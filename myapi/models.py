from authentication.models import CustomUser
from myapi.separate_song import SeparateSongThread
import os
from voiceMelody.settings import BASE_DIR
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class Song(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True, default="No Title")
    song = models.FileField(upload_to="media")
    voice = models.FileField(upload_to="media", null=True, blank=True)
    melody = models.FileField(upload_to="media", null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_separating = models.BooleanField(default=False)
    is_separated = models.BooleanField(default=False)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Song)
def my_handler(sender, instance: Song, **kwargs):
    if not instance.is_separated and not instance.is_separating:
        SeparateSongThread(instance).start()
