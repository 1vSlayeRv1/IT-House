from django.contrib import admin

from .models import MessageToSupport, SupportSection

class MessageToSupportAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date', 'profile_id', 'section_id')
    list_display_links = ('title', 'profile_id', 'section_id')
    search_fields = ('title', 'content', 'profile_id', 'section_id')

admin.site.register(MessageToSupport, MessageToSupportAdmin)
admin.site.register(SupportSection)