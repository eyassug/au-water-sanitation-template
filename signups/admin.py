from django.contrib import admin

# Register your models here.
from .models import SignUp 

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
        #code
    
    #code

#admin.site.register(SignUp, SignUpAdmin)