from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Board(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name