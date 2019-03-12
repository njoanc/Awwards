from django.test import TestCase
from .models import Article,tags,Editor
import datetime as dt

# Create your tests here.
class EditorTest(TestCase):
    def setUp(self):
        self.new_editor = Editor(first_name='Jeanne',last_name='Nyiramwiza',email='njoanc@gmail.com')
        self.new_editors = Editor(first_name='Jeanne',last_name='Nyiramwiza',email='njoanc@gmail.com')
       
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_editor,Editor))
    
    def test_save_editor(self):
        self.new_editor.save()
        length = Editor.objects.all()
        self.assertTrue(len(length) > 0)   

    def test_delete(self):
        delete_editor = Editor.objects.filter(id=1)
        delete_editor.delete()
        new_editors = Editor.objects.all()
        self.assertTrue(len(new_editors) == 0)   

    def test_update(self):
        self.new_editors.save()
        self.update_editor = Editor.objects.filter(first_name='Jeanne').update(first_name = 'Jehanne')
        self.updated_editor = Editor.objects.get(first_name='Jehanne')
        self.assertTrue(self.updated_editor.first_name,'Jehanne')
    
class Articletest(TestCase):
    def setUp(self):
        self.editor1 =  Editor(first_name='Jeanne',last_name='Nyiramwiza',email='njoanc@gmail.com')
        self.editor1.save()
        self.new_article = Article(title='OMG',post='Here we are',editor=self.editor1)
        self.new_article.save()

        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
    
    def test_save_article(self):
        self.editor1.save()
        self.new_article.save()
        length = Editor.objects.all()
        self.assertTrue(len(length) > 0)   

    def test_delete_article(self):
        delete_article = Article.objects.filter(id=1)
        delete_article.delete()
        new_articles = Article.objects.all()
        self.assertTrue(len(new_articles) == 0)   

    def test_update_article(self):
        self.new_article.save()
        self.update_article = Article.objects.filter(title='CNN').update(title = 'AirForceCrush')
        self.updated_article = Article.objects.get(title='AirForceCrush')
        self.assertTrue(self.updated_article.title,'AirForceCrush')

    def test_get_news(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)