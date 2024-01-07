from django.contrib import admin
from .models import *
from vaxapp.models import User_info
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountInline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = 'User_infos'

class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(User_info)
admin.site.register(Vaccine)
admin.site.register(Register)
admin.site.register(Schedule)
admin.site.register(Barangay)

