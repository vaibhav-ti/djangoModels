from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    project_slug = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectAccess(models.Model):
    user_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    project_id = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    created_by_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="project_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectService(models.Model):
    name = models.CharField(max_length=128)
    project_id = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    template_id = models.ForeignKey("templates.ServiceTemplate", on_delete=models.CASCADE)
    status = models.CharField(max_length=12, default="creating")
    repo_link = models.URLField(null=True, blank=True)
    configuration = models.JSONField()
    private_key_rsa = models.TextField(blank=True, null=True)
    public_key_rsa = models.TextField(blank=True, null=True)
    created_by_id = models.ForeignKey("accounts.User", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





