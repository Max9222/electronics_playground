from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    date_start = models.DateField(default=timezone.now, verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Partner(models.Model):
    FACTORY = 0
    RETAIL = 1
    SOLE = 2
    LEVELS = (
        (FACTORY, 'завод'),
        (RETAIL, 'розничная сеть'),
        (SOLE, 'индивидуальный предприниматель'),
    )

    levels = models.IntegerField(default=FACTORY, choices=LEVELS, verbose_name='уровень')
    title = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=100, verbose_name='номер дома')


