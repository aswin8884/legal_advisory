# Generated by Django 5.0.6 on 2024-07-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0025_advocate_registration_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate_registration',
            name='fees',
            field=models.IntegerField(default=0),
        ),
    ]
