from django.contrib import admin

# Register your models here.
from .models import System

class SystemAdmin(admin.ModelAdmin):
    #code
    class Meta:
        model = System
        #code
    admin.site.register(System)