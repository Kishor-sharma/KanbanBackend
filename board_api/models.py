from django.db import models

# Create your models here.
class Board(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    userID      = models.SmallIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name