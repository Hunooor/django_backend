from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, )
    profile_picture = models.TextField(null=True, default=None)

    def __str__(self):
        return self.email
