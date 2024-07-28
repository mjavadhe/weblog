from django import forms
from .models import Post, Comment, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
