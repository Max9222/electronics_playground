# Generated by Django 5.0.2 on 2024-02-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0024_alter_partner_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='partner',
        ),
        migrations.AddField(
            model_name='partner',
            name='contact',
            field=models.ManyToManyField(to='chain.contact', verbose_name='контакты'),
        ),
    ]
