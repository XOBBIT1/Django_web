from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'

