from django.contrib import admin
from django.utils.safestring import mark_safe
from images.models import Image

from .models import MessageToSupport, SupportSection


class MessageImageSupportAdmin(admin.TabularInline):
    model = Image.support.through

    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image}" style="max-height: 200px;">')


class MessageToSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date',
                    'profile_id', 'section_id')
    list_display_links = ('title', 'profile_id', 'section_id')
    search_fields = ('title', 'content', 'profile_id', 'section_id')
    inlines = (MessageImageSupportAdmin, )


class SupportSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section')
    list_display_links = ('section',)
    search_fields = ('section', )


admin.site.register(MessageToSupport, MessageToSupportAdmin)
admin.site.register(SupportSection, SupportSectionAdmin)
