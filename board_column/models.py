from django.db import models

# Create your models here.
class BoardColumn(models.Model):
    boardID     = models.SmallIntegerField()
    columnID    = models.SmallIntegerField()
    capacity    = models.SmallIntegerField()
    limit       = models.SmallIntegerField()