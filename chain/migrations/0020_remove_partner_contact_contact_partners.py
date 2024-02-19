# Generated by Django 5.0.2 on 2024-02-18 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0019_remove_contact_partners_remove_partner_early_partner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='partners',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.partner'),
        ),
    ]
