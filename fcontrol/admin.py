from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fcontrol.models import Institution, Fridge, Controller, User, ControllerData
class SensorDataInLine(admin.TabularInline):
    model = ControllerData
    extra = 0
    readonly_fields = ('timestamp',)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('acc_name',)
#     list_per_page = 10
#     search_fields = ('acc_name',)
#
# class EmployeesAdmin(admin.ModelAdmin):
#     list_display = ('first_name','last_name','phone_number')
#     list_per_page = 10
#     search_fields = ('last_name',)

class FridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    search_fields = ('institution_name',)


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_per_page = 10
    search_fields = ('address',)


class ControllerAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    list_per_page = 10
    search_fields = ('address',)
    inlines = (SensorDataInLine,)

class ControllerDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity')
    list_per_page = 10
    search_fields = ('address',)


admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(ControllerData, ControllerDataAdmin)