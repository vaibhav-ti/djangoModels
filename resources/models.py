from django.db import models

# Create your models here.

class Resource(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, null=True)
    environment = models.ForeignKey('services.Environment', on_delete=models.CASCADE, null=True)
    resource_type = models.CharField(max_length=128)
    created = models.BooleanField(default=False)
    title = models.CharField(max_length=128, null=True)
    metadata_values = models.JSONField(max_length=128, null=True)
    user_input = models.JSONField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
