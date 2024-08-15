from django.contrib import admin

from user.models import UserModel


# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass
