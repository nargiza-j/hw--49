from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ('avatar', 'profile_url', 'about_info')


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
