from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class MyUserAdmin(UserAdmin):
    model = MyUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('department','degree',)}),
    )

# Register your models here.
admin.site.register(Department)
admin.site.register(Degree)
admin.site.register(MyUser,MyUserAdmin)