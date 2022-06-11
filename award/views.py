from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request,'index.html', {'posts': posts})

def profile(request):
    set = Profile.objects.all()
    
    return render(request, 'profile.html',{'set':set})

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f'Account created.Please login!')
            return redirect('login')
    else:
        form =UserRegisterForm()    
    
    return render(request,'users/register.html',{'form':form })
