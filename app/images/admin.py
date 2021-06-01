from django.contrib import admin
from .models import Image



class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
  



admin.site.register(Image, ImageAdmin)