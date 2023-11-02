# game/models.py
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Game(models.Model):
    RELEASE_STATUS_CHOICES = (
        ('Released', 'Released'),
        ('In Development', 'In Development'),
        ('On Hold', 'On Hold'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    release_status = models.CharField(
        max_length=20,
        choices=RELEASE_STATUS_CHOICES,
        default='In Development'
    )
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

 