# Generated by Django 5.0.6 on 2024-06-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False, verbose_name='Id rol')),
                ('nombreRol', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
