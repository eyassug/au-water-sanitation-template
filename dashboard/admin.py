from django.contrib import admin


from models import AccessCharacteristic, SectorPerformanceCategory, System, PriorityArea, AccessProperty, TenderProcedureProperty

#Register models


admin.site.register(AccessCharacteristic)
admin.site.register(SectorPerformanceCategory)
admin.site.register(System)
admin.site.register(PriorityArea)
admin.site.register(TenderProcedureProperty)
admin.site.register(AccessProperty)
