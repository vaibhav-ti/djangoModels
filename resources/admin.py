from django.contrib import admin

# Register your models here.
from .models import Resource, ServiciesEnviornment
admin.site.register(Resource)
admin.site.register(ServiciesEnviornment)