from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True, default="No Title")
    song = models.FileField(upload_to="media")
    voice = models.FileField(upload_to="media")
    melody = models.FileField(upload_to="media")

    def __str__(self):
        return self.title
