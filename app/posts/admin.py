from django.contrib import admin
from .models import Post, Profile, Comment, Role, FieldOfInterest


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'age', 'date_reg')
    list_display_links = ('user', 'firstname', 'date_reg')
    search_fields = ('user', 'firstname')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'profile_id', 'post_id')
    list_display_links = ('comment', 'profile_id', 'post_id')
    search_fields = ('comment', 'profile_id', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Role)
admin.site.register(FieldOfInterest)
