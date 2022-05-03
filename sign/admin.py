from django.contrib import admin

from sign.models import SignupForm

# Register your models here.
@admin.register(SignupForm)
class UserAdmin(admin.ModelAdmin):
    
    list_display = ("id","name","username","password","email")