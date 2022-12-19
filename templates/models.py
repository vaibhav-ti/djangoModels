from django.db import models

# Create your models here.


class TemplateVersion(models.Model):
    template = models.ForeignKey("templates.ServiceTemplate", on_delete=models.SET_NULL, null=True)
    version = models.FloatField(null=False)
    tag_name = models.CharField(max_length=128)
    commit = models.CharField(max_length=128)
    data_schema = models.JSONField()
    ui_schema = models.JSONField()
    default_data = models.JSONField()
    # this is a many to many relation
    # tags =
    description = models.CharField(max_length=128)


class ServiceTemplate(models.Model):
    name = models.CharField(max_length=128)
    base_repo = models.CharField(max_length=256)
    author_id = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TemplateTag(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

