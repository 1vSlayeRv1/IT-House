from django.contrib import admin
from django.utils.safestring import mark_safe

from images.models import Image
from .models import Profile, Role, FieldOfInterest



class EventProfileAdmin(admin.TabularInline):
    model = Profile.profile_event.through


class ProfileImageAdmin(admin.TabularInline):
    model = Image.profile.through
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image}" style="max-height: 200px;">')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname',
                    'lastname', 'email', 'created_at')
    list_diplay_links = ('user',)
    search_fields = ('user', 'email')
    inlines = (EventProfileAdmin, ProfileImageAdmin)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
