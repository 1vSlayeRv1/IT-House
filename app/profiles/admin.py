from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import FieldOfInterest, Profile, Role


class EventProfileAdmin(admin.TabularInline):
    model = Profile.profile_event.through


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname',
                    'lastname', 'email', 'created_at')
    list_diplay_links = ('user',)
    search_fields = ('user', 'email')
    readonly_fields = ['preview']
    inlines = (EventProfileAdmin,)

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.avatar.url}" style="max-height: 200px;">')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
