from django.db import models
from django.db.models.fields import related
from django.utils.safestring import mark_safe
from profiles.models import Profile
from posts.models import Post
from support.models import MessageToSupport
from .utilities import get_timestamp_path
class Image(models.Model):
    file = models.ImageField(blank=True, null=True,
                            verbose_name='изображение',
                            upload_to=get_timestamp_path)
    profile = models.ManyToManyField(Profile,blank=True, related_name='profile_image')
    post = models.ManyToManyField(Post, blank=True, related_name='post_image')
    support = models.ManyToManyField(MessageToSupport, blank=True, related_name='support_image')


    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'