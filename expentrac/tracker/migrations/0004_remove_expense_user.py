# Generated by Django 3.0.7 on 2020-07-10 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200710_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]