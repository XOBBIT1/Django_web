from django.urls import path
from .views import Home, PostDetail, AddPost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name="add-post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),
]

