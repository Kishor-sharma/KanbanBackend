from django.db import models

# Create your models here.
class Lanes(models.Model):
    name        = models.TextField(max_length=100, unique=True)
    index       = models.SmallIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    edited_at   = models.DateTimeField(auto_now=True)