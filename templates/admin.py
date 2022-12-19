from django.contrib import admin

# Register your models here.
from .models import TemplateVersion, ServiceTemplate, TemplateTag
admin.site.register(TemplateTag)
admin.site.register(ServiceTemplate)
admin.site.register(TemplateVersion)