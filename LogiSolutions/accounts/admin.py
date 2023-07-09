from django.contrib import admin
from django.contrib.auth import get_user_model

from LogiSolutions.accounts.models import Profile

UserModel = get_user_model()


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    pass