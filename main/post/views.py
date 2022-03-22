from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentsForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class Home(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ["-id"]


class Customer_posts(ListView):
    model = Post
    template_name = 'post/customer_posts.html'
    ordering = ["-id"]

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')


class AddComment(CreateView):
    model = Comment
    form_class = CommentsForm
    template_name = 'post/add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

