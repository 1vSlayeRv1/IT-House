from django.contrib import admin
from django.utils.safestring import mark_safe
from images.models import Image

from .models import Comment, Post


class ImagesInline(admin.TabularInline):
    model = Image.post.through
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image}" style="max-height: 200px;">')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title', 'date')

    inlines = (ImagesInline, )
    fileds = ('title', 'description', 'content')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'date', 'profile_id', 'post_id')
    list_display_links = ('comment', 'profile_id', 'post_id')
    search_fields = ('comment', 'profile_id', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
