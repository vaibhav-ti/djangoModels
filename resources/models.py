from django.db import models

# Create your models here.

class Resource(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    enviornment = models.ForeignKey('services.Environment', on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=128)
    created = models.BooleanField(default=False)
    metadata = models.JSONField(max_length=128)
    user_input = models.JSONField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
