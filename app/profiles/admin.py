from django.contrib import admin

from .models import Profile, Role, FieldOfInterest


class EventProfileAdmin(admin.TabularInline):
    model = Profile.profile_event.through


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', 'created_at')
    list_diplay_links = ('user',)
    search_fields = ('user', 'email')
    inlines = (EventProfileAdmin, )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
