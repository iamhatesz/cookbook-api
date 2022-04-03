from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.name
