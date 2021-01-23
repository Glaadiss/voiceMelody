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
        separator = Separator("spleeter:2stems")
        MEDIA_ROOT = os.path.join(BASE_DIR, "results")

        separator.separate_to_file(self.instance.song.path, MEDIA_ROOT)

        subject = f"Piosenka {self.instance.title} gotowa!"
        message = "Hello world"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            "bartekgladys@gmail.com",
        ]
        send_mail(subject, message, email_from, recipient_list)