from django.urls import path
from .views import Home, PostDetail, AddPost, DeletePost, Customer_posts, Like, AddComment

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('customer_posts', Customer_posts.as_view(), name='customer-posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name="add-post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),
    path('like/<int:pk>', Like, name='like_post'),
    path('add_comment/<int:pk>/comment', AddComment.as_view(), name="add-comment"),
]

