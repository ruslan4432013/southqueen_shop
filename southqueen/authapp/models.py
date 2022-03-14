from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
