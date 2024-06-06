from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, Location

admin.site.register(CustomUser)
admin.site.register(Location)
