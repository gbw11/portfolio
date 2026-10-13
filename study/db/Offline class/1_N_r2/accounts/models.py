from django.db import models

# Create your models here.
# AbstractUser : User 관련된 기본적인 필드를 제공
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers'
    )