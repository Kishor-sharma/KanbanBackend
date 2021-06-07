from django.db import models
from django.db.models.fields import SmallIntegerField

# Create your models here.
class Task(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    status      = models.BooleanField()
    columnID    = models.SmallIntegerField()
    boardID     = SmallIntegerField()

    def __str__(self):
        return self.title