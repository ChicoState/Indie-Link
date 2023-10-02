# game/models.py
from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
=======
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()

>>>>>>> 0d8ef7b (Adds user game entries, display and delete)
    def __str__(self):
        return self.name
