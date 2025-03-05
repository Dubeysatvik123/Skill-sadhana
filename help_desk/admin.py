from django.contrib import admin
from .models import HelpDeskQuery

@admin.register(HelpDeskQuery)
class HelpDeskQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_resolved')
    search_fields = ('name', 'email', 'query')
    list_filter = ('is_resolved', 'created_at')
    ordering = ('-created_at',)
