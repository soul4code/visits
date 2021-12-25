from django.contrib import admin
from store.models import Employee, Store, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("date", "store", "coordinates")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
