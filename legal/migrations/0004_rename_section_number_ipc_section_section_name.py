# Generated by Django 5.0.6 on 2024-06-25 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0003_ipc_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipc_section',
            old_name='section_number',
            new_name='section_name',
        ),
    ]
