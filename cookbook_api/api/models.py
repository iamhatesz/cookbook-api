from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(default="")
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    created_on = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.name
