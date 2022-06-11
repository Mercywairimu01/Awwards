from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Profile
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request,'index.html', {'posts': posts})

def profile(request):
    set = Profile.objects.all()
    
    return render(request, 'profile.html',{'set':set})

