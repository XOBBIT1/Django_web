from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

class Home(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ["-id"]

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')

