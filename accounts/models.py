from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ad_username = models.CharField(max_length=(128), null=True)
    github_username = models.CharField(max_length=(128), null=True)
    github_token = models.CharField(max_length=(128), null=True)
    google_access_token = models.CharField(max_length=(2048), null=True)
    google_refresh_token = models.CharField(max_length=(128), null=True)
