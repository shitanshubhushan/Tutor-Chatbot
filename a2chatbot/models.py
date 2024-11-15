from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    def __unicode__(self):
        return 'id='+ str(self.pk)

class Assistant(models.Model):
    assistant_id = models.TextField(verbose_name = "Assistant ID")
    video_name = models.CharField(verbose_name= "videoname", default = '', max_length=100)
    vector_store_id = models.TextField(verbose_name='Vector store ID')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True)

class Message(models.Model):
    conversation = models.ForeignKey(Participant, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_id = models.IntegerField(default=1)