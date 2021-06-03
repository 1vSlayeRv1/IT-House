from django.db import models

from images.helpers import resize_logo
from profiles.models import Profile
from posts.models import Post
from support.models import MessageToSupport
from .utilities import get_timestamp_path


class Image(models.Model):
    file = models.ImageField(blank=True, null=True,
                             verbose_name='изображение',
                             upload_to=get_timestamp_path)
    profile = models.ManyToManyField(
        Profile, blank=True, related_name='profile_image')
    post = models.ManyToManyField(Post, blank=True, related_name='post_image')
    support = models.ManyToManyField(
        MessageToSupport, blank=True, related_name='support_image')

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)

        if self.file:
            resize_logo(self)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.file.storage, self.file.path
        # Delete the model before the file
        super(Image, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    def __str__(self):
        return self.file.url

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
