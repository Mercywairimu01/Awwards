from django.db import models
from django.contrib.auth.models import User
from PIL  import Image
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images',null =True)
    title = models.CharField(max_length = 60, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    livelink = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()
