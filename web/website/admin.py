from __future__ import unicode_literals
from django.utils.html import format_html
from django.contrib import admin
from .models import service, team, about, value, home
from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput, Textarea

@admin.register(service)
class serviceAdmin(ImportExportModelAdmin):
    list_display = ['id','headline','group']
    pass

@admin.register(team)
class teamAdmin(ImportExportModelAdmin):
    list_display = ['id','firstname', 'lastname']
    pass

@admin.register(about)
class serviceAdmin(ImportExportModelAdmin):
    list_display = ['headline',]
    pass

@admin.register(value)
class serviceAdmin(ImportExportModelAdmin):
    list_display = ['headline',]
    pass

@admin.register(home)
class serviceAdmin(ImportExportModelAdmin):
    list_display = ['headline',]
    pass