from django.db import models

# Create your models here.
class Board(models.Model):
    name        = models.TextField(max_length=100)
    userID      = models.SmallIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)