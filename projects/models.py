from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    project_slug = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectAccess(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
