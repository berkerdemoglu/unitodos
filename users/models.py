from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    university = models.CharField(
        max_length=80,
        choices=settings.UNIVERSITIES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Profile of {self.owner}'
