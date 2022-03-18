from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'customers', 'text')

        widgets = {
            'title': forms.TimeInput(attrs={
                'class':'form-control'
            }),
            'customers': forms.TimeInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.TimeInput(attrs={
                'class': 'form-control'
            }),
        }