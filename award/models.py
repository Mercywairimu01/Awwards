from django.db import models
from django.contrib.auth.models import User
from PIL  import Image
from django.db.models import Q
from django.urls import reverse
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
    def search_projects(cls, searchterm):
        searchresults = cls.objects.filter(Q(title__icontains=searchterm) | Q(description__icontains=searchterm) | Q(author__username__icontains=searchterm))
        return searchresults
    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()
        
    @classmethod
    def user_post(cls, username):
        posts = cls.objects.filter(author__username=username)
        return posts
        
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
      ordering = ['-id']
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images', default='default.png')
    bio = models.TextField(max_length=500, default="Coffee and Code")
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs):
        super().save( **kwargs)
        img= Image.open(self. profile_picture.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 2500)
            img.thumbnail(output_size)
            img.save(self. profile_picture.path)
    
class Rate(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0)
    usability = models.IntegerField(choices=rating, default=0)
    content = models.IntegerField(choices=rating, default=0)
    review = models.CharField(max_length=300, blank=True, null=True)
    average = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = cls.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'
      
       