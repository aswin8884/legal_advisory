# Generated by Django 5.0.6 on 2024-06-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0015_remove_request_work_admin_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='status',
            field=models.CharField(default=False, max_length=25, null=True),
        ),
    ]
