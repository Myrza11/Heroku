from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Content(models.Model):
    namegame = models.CharField(max_length=20)
    content = models.TextField()
    photos = models.ImageField(upload_to='photos/%Y/%m/%d')
    category = ForeignKey('Category', on_delete=CASCADE)

    def __str__(self):
        return self.namegame

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__ (self):
        return self.title