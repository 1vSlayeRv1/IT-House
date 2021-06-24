from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Event, EventGroup, Office


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date_start', 'date_end')
    list_display_links = ('name',)
    search_fields = ('name',)
    readonly_fields = ['preview']
    fields = ('name', 'description', 'office', 'date_start',
              'date_end', 'file', 'preview')

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file}" style="max-height: 200px;">')


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name',)
    search_fields = ('name',)


class EventGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'profile', 'status')
    list_display_links = ('id', 'event', 'profile')
    ordering = ['event']


admin.site.register(Event, EventAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(EventGroup, EventGroupAdmin)
