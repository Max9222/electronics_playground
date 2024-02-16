from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


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
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='номер дома', **NULLABLE)
    product = models.ManyToManyField(Product, verbose_name='продукт')
    early_partner = models.ForeignKey('Partner', on_delete=models.CASCADE, verbose_name='поставщик предыдущий')
    backlog = models.IntegerField(default=0, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return f'{self.title} уровень: {self.levels}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
