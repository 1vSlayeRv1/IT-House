from django.contrib import admin
from .models import Event, Office
from images.models import Image
from django.utils.safestring import mark_safe


class ProfileEventAdmin(admin.TabularInline):
    model = Event.profile.through


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_start', 'date_end')
    list_display_links = ('name',)
    search_fields = ('name',)
    readonly_fields = ['preview']
    fields = ('name', 'description', 'date_start',
              'date_end', 'file', 'preview')
    inlines = (ProfileEventAdmin, )

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file}" style="max-height: 200px;">')


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Event, EventAdmin)
admin.site.register(Office, OfficeAdmin)
