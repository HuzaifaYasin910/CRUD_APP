from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=17, unique=True,blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_published = models.DateField()
    author = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
