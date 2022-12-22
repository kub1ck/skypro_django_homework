from django.db import models

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=30)
    items = models.ManyToManyField(Ad)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
