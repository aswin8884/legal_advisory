# Generated by Django 5.0.6 on 2024-06-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0019_cases_advocate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='current_date',
            field=models.DateField(null=True),
        ),
    ]
