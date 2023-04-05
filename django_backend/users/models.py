from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    reference_id = models.TextField(default=uuid.uuid4, null=False, unique=True)
    email = models.EmailField(unique=True, null=False)
    profile_picture = models.TextField(null=True, default=None)

    def __str__(self):
        return self.email
