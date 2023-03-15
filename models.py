from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField()

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=64, unique=True)
    birthday_year = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    

class Book(models.Model):

    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
