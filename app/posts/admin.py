from django.contrib import admin
from .models import Post,  Comment
from django.utils.safestring import mark_safe
from images.models import Image

class ImagesInline(admin.TabularInline):
    model = Image.post.through
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    list_display_links = ('title', 'date')
    search_fields = ('title', 'date')
    readonly_fields = ['preview']
    inlines = (ImagesInline, )
    fileds = ('title', 'description', 'content', 'preview')
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.post_image.url}" style="max-height: 200px;">')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date', 'profile_id', 'post_id')
    list_display_links = ('comment', 'profile_id', 'post_id')
    search_fields = ('comment', 'profile_id', 'post_id')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
