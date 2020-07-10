# Generated by Django 3.0.7 on 2020-07-10 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date of expense')),
                ('item', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, choices=[('CLO', 'Clothing'), ('FOOD', 'Food'), ('FUEL', 'Fuel'), ('RENT', 'Rent'), ('UTI', 'Utilities'), ('PHN', 'Phone'), ('EDU', 'Education'), ('MISC', 'Miscellaneous')], max_length=4, null=True)),
                ('amount', models.FloatField()),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
