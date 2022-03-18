from django.urls import path
from .views import Home, PostDetail, AddPost

urlpatterns = [
    path('', Home.as_view()),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name="add-post"),

]

