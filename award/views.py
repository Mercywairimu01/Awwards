from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse,Http404,HttpResponse
from .models import Post,Profile,Rate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserForm,PostForm,ProfileForm,RateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView, UpdateView
from django.contrib.auth.models import User
from rest_framework import viewsets,serializers
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
from .permissions import IsAdminOrReadOnly



# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request,'index.html', {'posts': posts})

def register(request):
    if request.user.is_authenticated:
        raise Http404
    else:
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

def profile(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')

    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        current_profile = Profile.objects.get(user_id = request.user)
        current_post = Post.user_post(request.user)
          

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_post':current_post,
        'current_profile':current_profile
    }

    return render(request, 'users/profile.html', context)

def user_profile(request, id):
   try:
     user_detail = Profile.objects.get(id=id)
     current_post = Post.user_post(user_detail.username)
     if request.user.username == str(user_detail.username):
       return redirect('profile')
     else:
       return render(request, 'userprofile.html', {'userdetail':user_detail, ' current_post': current_post})
   except Profile.DoesNotExist:
      return HttpResponseRedirect(" Sorry the Page You Looking For Doesn't Exist.")

def post(request):
  if request.method == 'POST':
    postform = PostForm(request.POST, request.FILES)
    if postform.is_valid:
      post = postform.save(commit=False)
      post.author = request.user
      post.save()
    return redirect('index')

  postform = PostForm()
  params = {'postform':postform,}
  return render(request, 'post.html', params)

def postdetails(request, id):
    post = Post.objects.get(id=id)
    form = RateForm()
    user  = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.post = post
            rate.save()
            
            return HttpResponse('Thank you for your feedback')
    params = {
        'post':post,
        'form':form,
       
    }
    return render(request, 'post_detail.html', params)



class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def search_projects(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchresults = Post.search_projects(search_term)
    return render(request, 'search.html', {'searchresults':searchresults, 'search_term':search_term})
  else:
    return redirect('index')

