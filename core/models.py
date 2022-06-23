from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')


