# Generated by Django 3.2 on 2021-06-12 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='name',
        ),
    ]