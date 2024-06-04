from django.contrib import admin
from django.contrib.auth.hashers import make_password

from administration.models import AdminStaff


@admin.register(AdminStaff)
class AdminStaffAdmin(admin.ModelAdmin):
    list_display = ('personnel_number', 'first_name', 'last_name', 'phone', 'role',)
    list_filter = ('role',)
    search_fields = ('personnel_number', 'first_name', 'last_name', 'phone')
    fields = ('personnel_number', 'first_name', 'last_name', 'phone', 'role', 'password')

    def save_model(self, request, obj, form, change):
        if change:
            if "password" in form.changed_data:
                obj.password = make_password(obj.password)
        else:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
