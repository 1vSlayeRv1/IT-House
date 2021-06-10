from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'mini_preview')
    fields = ('file', 'preview', 'profile', 'post', 'support')
    readonly_fields = ['preview', 'mini_preview']

    def mini_preview(self, obj):
        return mark_safe(
            f'<img src="{obj.file.url}" style="max-height: 50px;">')

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.file.url}" style="max-height: 200px;">')


admin.site.register(Image, ImageAdmin)
