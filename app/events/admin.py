from django.contrib import admin
from .models import Event, Office


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_start', 'date_end')
    list_display_links = ('name',)
    search_fields = ('name',)


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Event, EventAdmin)
admin.site.register(Office, OfficeAdmin)
