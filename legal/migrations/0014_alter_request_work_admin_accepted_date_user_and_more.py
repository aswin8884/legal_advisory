# Generated by Django 5.0.6 on 2024-06-26 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0013_request_work_admin_accepted_date_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_work_admin',
            name='accepted_date_user',
            field=models.DateField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='request_work_admin',
            name='user_id',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration'),
        ),
    ]
