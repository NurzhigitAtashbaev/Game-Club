from django.contrib import admin
from .models import Computer


class ComputerDisplay(admin.ModelAdmin):
    list_display = ('number', 'busy')


admin.site.register(Computer, ComputerDisplay)
