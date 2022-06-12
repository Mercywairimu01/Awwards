from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostUpdateView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('', PostListView.as_view(),name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name ='post_detail.html'), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name ='post_form.html'), name='post-update'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register,name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name ='logout'),
    path('search/', views.search_projects, name='search'),
  
]