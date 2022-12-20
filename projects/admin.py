from django.contrib import admin

# Register your models here.
from .models import Project, ProjectAccess
admin.site.register(Project)
admin.site.register(ProjectAccess)
