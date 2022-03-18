from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    customers = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField('Описание')
    image_post = models.ImageField(null=True, blank=True, upload_to="images/")
    image_profile_user = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        verbose_name = 'User_post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title + '|' + str(self.customers)

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))