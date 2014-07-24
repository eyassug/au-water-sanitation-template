from django.contrib import admin

# Register your models here.
from .models import SectorPerformanceCategory

class SectorPerformanceCategoryAdmin(admin.ModelAdmin):
    #code
    class Meta:
        model = SectorPerformanceCategory
        #code
    admin.site.register(SectorPerformanceCategory)
