from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from dashboard.models import UserCountry
from forms import CustomPriortyAreaForm


from models import SectorCategory,  Technology, PriorityArea, FacilityCharacter, TenderProcedureProperty, CommunityApproachType, Partner, Event

#Register models


admin.site.register(SectorCategory)
admin.site.register(Technology)
admin.site.register(PriorityArea)
admin.site.register(TenderProcedureProperty)
admin.site.register(FacilityCharacter)
#admin.site.register(CommunityApproachType)
admin.site.register(Partner)
admin.site.register(Event)



# Define an inline admin descriptor for UserCountry (singleton)
class UserCountryInline(admin.TabularInline):
    model = UserCountry
    can_delete = False
    verbose_name_plural = 'Country'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserCountryInline, )
    
class PriorityAreaAdmin(admin.ModelAdmin):
    form = CustomPriortyAreaForm
    exclude = ['country']
    def save_model(self, request, obj, form, change):
        obj.country = request.user.usercountry.country
        obj.save()
        
        
     
    #code


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(PriorityArea)
admin.site.register(PriorityArea,PriorityAreaAdmin)