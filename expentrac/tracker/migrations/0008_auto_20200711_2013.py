# Generated by Django 3.0.7 on 2020-07-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_expense_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(blank=True, choices=[('Clothing', 'Clothing'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Rent', 'Rent'), ('Utilities', 'Utilities'), ('Phone', 'Phone'), ('Education', 'Education'), ('Miscellaneous', 'Miscellaneous')], max_length=20, null=True),
        ),
    ]
