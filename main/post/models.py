from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    customers = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField('Описание')
    image_post = models.ImageField(null=True, blank=True, upload_to="images/")
    image_profile_user = models.ImageField(null=True, blank=True, upload_to="images/")
    dara_post = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_post")

    class Meta:
        verbose_name = 'User_post'
        verbose_name_plural = 'Posts'

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.customers) +'|'+ str(self.dara_post)


    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_img = models.ImageField(null=True, blank=True, upload_to="images/profile")


    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=False)
    name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    data_comment = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))