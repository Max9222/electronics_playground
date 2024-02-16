# Generated by Django 5.0.2 on 2024-02-16 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0002_partner_date_create_alter_partner_backlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='early_partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.partner', verbose_name='поставщик предыдущий'),
        ),
    ]
