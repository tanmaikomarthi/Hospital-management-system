# Generated by Django 4.2.7 on 2023-12-08 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='doctor_login',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
