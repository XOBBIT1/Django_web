from django.urls import path
from .views import UserRegistration


urlpatterns = [
    path('members/', UserRegistration.as_view(), name='register'),
]

