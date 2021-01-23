import os
from voiceMelody.settings import BASE_DIR
import threading
from spleeter.separator import Separator
from django.core.mail import send_mail
from django.conf import settings


class SeparateSongThread(threading.Thread):
    def __init__(self, instance, **kwargs):
        self.instance = instance
        super(SeparateSongThread, self).__init__(**kwargs)

    def run(self):
<<<<<<< HEAD

        self.instance.is_separating = True
        self.instance.save()
        separator = Separator("spleeter:2stems")
        MEDIA_ROOT = os.path.join(BASE_DIR, "media")

        separator.separate_to_file(self.instance.song.path, MEDIA_ROOT)

        self.instance.is_separating = False
        self.instance.is_separated = True
        song_base = "".join(self.instance.song.name.split(".")[:-1])
        self.instance.voice.name = f"{song_base}/vocals.wav"
        self.instance.melody.name = f"{song_base}/accompaniment.wav"
        self.instance.save()
        subject = f"Piosenka {self.instance.title} gotowa!"
        message = "Hello world"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.instance.user.email]
=======
        separator = Separator("spleeter:2stems")
        MEDIA_ROOT = os.path.join(BASE_DIR, "results")

        separator.separate_to_file(self.instance.song.path, MEDIA_ROOT)

        subject = f"Piosenka {self.instance.title} gotowa!"
        message = "Hello world"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            "bartekgladys@gmail.com",
        ]
>>>>>>> 42aaa62... Add SeparateSongThread
        send_mail(subject, message, email_from, recipient_list)