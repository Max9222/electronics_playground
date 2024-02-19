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


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Partner(models.Model):
    FACTORY = 0
    RETAIL = 1
    SOLE = 2
    LEVELS = (
        (FACTORY, 'завод'),
        (RETAIL, 'розничная сеть'),
        (SOLE, 'индивидуальный предприниматель'),
    )
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    levels = models.IntegerField(default=FACTORY, choices=LEVELS, verbose_name='уровень')
    contact = models.ManyToManyField(Contact, verbose_name='контакты')
    product = models.ManyToManyField(Product, verbose_name='продукты')
    early_partner = models.ForeignKey('Partner', on_delete=models.CASCADE, verbose_name='поставщик предыдущий', **NULLABLE)
    backlog = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    date_create = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
