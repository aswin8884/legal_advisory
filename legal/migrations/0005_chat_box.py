# Generated by Django 5.0.6 on 2024-06-25 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0004_rename_section_number_ipc_section_section_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, null=True)),
                ('current_time', models.TimeField()),
                ('current_date', models.DateField()),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
            ],
        ),
    ]
