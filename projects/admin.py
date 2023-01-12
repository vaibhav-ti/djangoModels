from django.contrib import admin

# Register your models here.
from .models import Project, ProjectAccess, ProjectEnvironment
admin.site.register(Project)
admin.site.register(ProjectAccess)
admin.site.register(ProjectEnvironment)
