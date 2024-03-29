# Generated by Django 5.0.2 on 2024-02-16 18:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('model', models.CharField(max_length=150, verbose_name='модель')),
                ('date_start', models.DateField(default=django.utils.timezone.now, verbose_name='дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.IntegerField(choices=[(0, 'завод'), (1, 'розничная сеть'), (2, 'индивидуальный предприниматель')], default=0, verbose_name='уровень')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='улица')),
                ('house_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='номер дома')),
                ('backlog', models.IntegerField(blank=True, default=0, null=True, verbose_name='задолженность')),
                ('early_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chain.partner', verbose_name='поставщик предыдущий')),
                ('product', models.ManyToManyField(to='chain.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
    ]
