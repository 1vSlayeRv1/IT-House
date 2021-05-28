from django.contrib import admin
from .models import Post,  Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'profile_id', 'post_id')
    list_display_links = ('comment', 'profile_id', 'post_id')
    search_fields = ('comment', 'profile_id', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
