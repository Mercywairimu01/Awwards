from django.test import TestCase
from .models import Post,Profile,Rate
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    '''
    Profile model tests
    '''
    def setUp(self):
        self.user = User(id=1, username='mercy', password='pre123456')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

class Testpost(TestCase):
    def setUp(self):
        self.post = Post(title='Delani Studion', image='test.jpg', author= User.objects.create(username='mercy'), description='a clone for delani studio', livelink='http://google.com/?search=this+is+amazing')
        self.user = User(id=1, username='mercy', password='pre123456')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save(self):
        self.post.save()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_projects('test')
        self.assertFalse(len(post) > 0)

class TestRate(TestCase):
    def setUp(self):
        self.post = Post(title='Delani Studion', image='test.jpg', author= User.objects.create(username='mercy'), description='a clone for delani studio', livelink='http://google.com/?search=this+is+amazing')
        self.user = User(id=1, username='mercy', password='pre123456')
        self.rating = Rate.objects.create(id=1, design=6, usability=7, content=9, user=self.user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)

       