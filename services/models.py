from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=128)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    template = models.ForeignKey("templates.TemplateVersion", on_delete=models.CASCADE)
    status = models.CharField(max_length=12, default="creating")
    repo_link = models.URLField(null=True, blank=True)
    configuration = models.JSONField()
    private_key_rsa = models.TextField(blank=True, null=True)
    public_key_rsa = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Environment(models.Model):
    name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    output = models.JSONField(null=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deployment_resources = models.JSONField(null=True)
