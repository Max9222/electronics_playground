# Generated by Django 5.0.2 on 2024-02-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_managers_remove_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=35, verbose_name='user name'),
        ),
    ]