import os
from voiceMelody.settings import BASE_DIR
import threading
from spleeter.separator import Separator
from django.core.mail import send_mail
from django.conf import settings


class SeparateSongThread(threading.Thread):
    def __init__(self, instance, **kwargs):
        self.instance = instance

    def run(self):

        self.instance.is_separating = True
        self.instance.save()
        separator = Separator("spleeter:2stems")
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")


        self.instance.is_separating = False
        self.instance.is_separated = True
        song_base = "".join(self.instance.song.name.split(".")[:-1])
        self.instance.voice.name = f"{song_base}/vocals.wav"
        self.instance.melody.name = f"{song_base}/accompaniment.wav"
        self.instance.save()
        subject = f"Piosenka {self.instance.title} gotowa!"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.instance.user.email]

