from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'biography', 'birth_date']

admin.site.register(Profile, ProfileAdmin)


###### or.....
#class ProfileInline(admin.TabularInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = 'Profile'

#class UserAdmin(BaseUserAdmin):
#    inlines = (ProfileInline,)

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)