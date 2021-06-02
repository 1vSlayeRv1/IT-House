from django.contrib import admin
from .models import Image
from django.utils.safestring import mark_safe


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
    fields = ('file', 'preview', 'profile', 'post', 'support')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" style="max-height: 200px;">')

admin.site.register(Image, ImageAdmin)