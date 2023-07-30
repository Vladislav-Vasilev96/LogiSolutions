from django.contrib import admin
from django.contrib.auth import get_user_model

from LogiSolutions.accounts.models import Profile, CustomUser

UserModel = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'is_superuser', 'is_staff')
    search_fields = ('email',)



@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('get_full_name','age', 'type','user')
    ordering = ('first_name', 'last_name', )
    search_fields = ('email',)