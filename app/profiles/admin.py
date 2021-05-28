from django.contrib import admin

from .models import Profile, Role, FieldOfInterest


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'email', 'date_reg')
    list_diplay_links = ('user',)
    search_fields = ('user', 'email')
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
