# Generated by Django 5.0.2 on 2024-02-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0015_remove_partner_early_partner_remove_partner_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='partner',
        ),
    ]
