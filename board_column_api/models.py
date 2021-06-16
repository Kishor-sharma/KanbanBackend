from django.db import models

# Create your models here.
class BoardColumn(models.Model):
    board_id    = models.SmallIntegerField()
    column_id   = models.SmallIntegerField()
    capacity    = models.SmallIntegerField(default=20)
    limit       = models.SmallIntegerField(default=5)