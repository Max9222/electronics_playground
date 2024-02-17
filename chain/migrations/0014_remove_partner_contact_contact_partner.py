# Generated by Django 5.0.2 on 2024-02-17 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0013_contact_remove_partner_city_remove_partner_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.partner', verbose_name='поставщик'),
        ),
    ]