from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=(150), null=False)
    password = models.CharField(max_length=(128), null=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, null=False)
    first_name = models.CharField(max_length=(150), null=True)
    last_name = models.CharField(max_length=(150), null=True, default="")
    ad_username = models.CharField(max_length=(128), null=True)
    github_username = models.CharField(max_length=(128), null=True)
    github_token = models.CharField(max_length=(128), null=True)
    google_access_token = models.CharField(max_length=(2048), null=True)
    google_refresh_token = models.CharField(max_length=(128), null=True)

    projects = models.ManyToManyField("projects.Project", through="projects.ProjectAccess",
                                      through_fields=('user_id', 'project_id'))


class AuthToken(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)