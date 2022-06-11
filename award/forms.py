from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile
from django.forms.widgets import TextInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
       model = Profile
       fields = '__all__'
       exclude = ['username']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'description', 'livelink',)
        exclude = ['author',]
        widgets = {
            'title':TextInput(attrs={
            'placeholder': 'Project Title...',
        }),
        'livelink': TextInput(attrs={
            'placeholder': 'Project live link...',
        })
    }