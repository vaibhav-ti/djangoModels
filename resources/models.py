from django.db import models

# Create your models here.

class Resource(models.Model):
    project_id = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    service_id = models.ForeignKey('projects.ProjectService', on_delete=models.CASCADE)
    enviornment_id = models.ForeignKey('resources.ServiciesEnviornment', on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    user_input = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ServiciesEnviornment(models.Model):
    name = models.CharField(max_length=128)
    branch_name = models.CharField(max_length=128)
    service_id = models.ForeignKey('projects.ProjectService', on_delete=models.CASCADE)
    output = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)