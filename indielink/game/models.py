# game/models.py
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    def __str__(self):
        return self.name
