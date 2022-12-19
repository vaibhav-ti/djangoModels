from django.contrib import admin

# Register your models here.
from .models import Project, ProjectAccess, ProjectService
admin.site.register(Project)
admin.site.register(ProjectAccess)
admin.site.register(ProjectService)