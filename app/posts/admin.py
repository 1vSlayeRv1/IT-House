from django.contrib import admin
from .models import Post, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'age', 'date_reg')
    list_display_links = ('user', 'firstname', 'date_reg')
    search_fields = ('user', 'firstname')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title', 'date')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
