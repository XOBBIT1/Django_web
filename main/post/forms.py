from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'customers', 'text', 'image_post', 'image_profile_user')

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'customers': forms.Select(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'elder',
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'name', 'text')

        widgets = {
            'post': forms.Select(attrs={
                'class':'form-control'
            }),
            'name': forms.Select(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'elder',
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }