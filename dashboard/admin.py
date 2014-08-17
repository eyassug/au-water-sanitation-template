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
    list_display = UserAdmin.list_display + ('country',)
        
    def country(self,obj):
        return obj.usercountry.country.name
    
class PriorityAreaAdmin(admin.ModelAdmin):
    form = CustomPriortyAreaForm
    list_display = ['name','country']
    
    def queryset(self,request):
        qs = super(PriorityAreaAdmin,self).queryset(request)
        if request.user.is_superuser:
            return qs
        user_country = request.user.usercountry.country
        return qs.filter(country__id=user_country.id)
        
    
    def get_form(self,request,obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('country')
        return super(PriorityAreaAdmin,self).get_form(request,obj,**kwargs)
    
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser():
            obj.country = request.user.usercountry.country
        obj.save()
    def get_country(self, obj):    
            return obj.country.name
     
    #code


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(PriorityArea)
admin.site.register(PriorityArea,PriorityAreaAdmin)