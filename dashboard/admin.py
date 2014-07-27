from django.contrib import admin


from models import SectorCategory,  Technology, PriorityArea, FacilityCharacter, TenderProcedureProperty, CommunityApproachType, Partner, Event

#Register models


admin.site.register(SectorCategory)
admin.site.register(Technology)
admin.site.register(PriorityArea)
admin.site.register(TenderProcedureProperty)
admin.site.register(FacilityCharacter)
admin.site.register(CommunityApproachType)
admin.site.register(Partner)
admin.site.register(Event)