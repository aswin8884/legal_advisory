# Generated by Django 5.0.6 on 2024-06-26 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0009_cases_accepted_alter_cases_posted_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cases',
            old_name='accepted',
            new_name='status',
        ),
    ]