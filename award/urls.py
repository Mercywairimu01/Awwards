from django.urls import path,include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)


urlpatterns = [
    path('',views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('profile/',views.profile, name='profile'),
    path('search/', views.search_projects, name='search'),
    path('postdetails/<int:id>/', views.postdetails, name='postdetails'),
    path('userprofile/<int:id>', views.user_profile, name='userprofile'),
    path('post/', views.post, name='post'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/',views.register,name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name ='logout'),
   
]