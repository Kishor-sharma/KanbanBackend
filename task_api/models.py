from django.db import models
from board_api.models import Board
from column_api.models import Lanes

# Create your models here.
class Task(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    status      = models.BooleanField()
    column      = models.ForeignKey(Lanes, on_delete=models.CASCADE)
    board       = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title