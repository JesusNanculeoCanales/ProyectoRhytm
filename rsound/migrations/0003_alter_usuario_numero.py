# Generated by Django 5.0.6 on 2024-06-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsound', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
