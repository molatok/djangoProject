from django.db import models


class Categories(models.Model):
    STATUS = [
        ('draft', 'Черновик категории'),
        ('published', 'Размещенная категория'),
        ('closed', 'Закрытая категория')
    ]

    status = models.CharField(max_length=30, choices=STATUS, default='draft')
    name = models.CharField(max_length=50)


class Ads(models.Model):
    STATUS = [
        ('draft', 'Черновик объявления'),
        ('published', 'Опубликованное объявление'),
        ('closed', 'Снято с публикации')
    ]

    status = models.CharField(max_length=50, choices=STATUS, default='draft')
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(max_length=5)
