from django.contrib import admin

# Register your models here.
from .models import User, AuthToken
admin.site.register(User)
admin.site.register(AuthToken)
