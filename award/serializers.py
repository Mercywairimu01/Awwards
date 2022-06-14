from rest_framework import serializers
from .models import Profile, Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'title', 'image', 'author', 'description', 'livelink', 'url')

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile 
    fields = [ 'profile_picture', 'bio', 'location', 'contact']


class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  post = PostSerializer(read_only=True, many=True)

  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'profile', 'post']
