from django.contrib import admin

# Register your models here.
from .models import TenderProcedureProperty

class TenderProceduerPropertyAdmin(admin.ModelAdmin):
    #code
    class Meta:
        model = TenderProcedureProperty
        #code
    admin.site.register(TenderProcedureProperty)
