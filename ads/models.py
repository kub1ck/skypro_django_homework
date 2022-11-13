from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=200)
