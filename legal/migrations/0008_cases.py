# Generated by Django 5.0.6 on 2024-06-25 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0007_alter_messages_advocate_id_alter_messages_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('posted_date', models.DateField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration')),
            ],
        ),
    ]
