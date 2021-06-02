from django.contrib import admin

from .models import Profile, Role, FieldOfInterest


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', 'created_at')
    list_diplay_links = ('user',)
    search_fields = ('user', 'email')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
