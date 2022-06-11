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
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images', default='default.png')
    bio = models.TextField(max_length=500, default="Coffee and Code")
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
        