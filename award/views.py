from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserForm,PostForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView, UpdateView
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request,'index.html', {'posts': posts})

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

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

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

class PostListView(ListView):
    model = Post
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
    
class PostDetailView(DetailView):
    model = Post    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image','title', 'description','livelink']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def search_projects(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchresults = Post.search_projects(search_term)
    return render(request, 'search.html', {'searchresults':searchresults, 'search_term':search_term})
  else:
    return redirect('index')
