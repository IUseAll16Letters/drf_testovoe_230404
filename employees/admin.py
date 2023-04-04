from django.contrib import admin

from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_second', 'dept', 'position', 'salary', 'age')
    list_editable = ('salary', 'age')
    list_display_links = ('id', 'name_second')
    search_fields = ('name_second', )
    list_filter = ('dept', 'position', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'head')
    list_editable = ('name', )
    search_fields = ('name', )
    list_filter = ('name',)
