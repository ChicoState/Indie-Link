# game/models.py
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
