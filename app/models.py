from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Note(models.Model):
    NOTE_TYPES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=NOTE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)