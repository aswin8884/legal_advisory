# Generated by Django 5.0.6 on 2024-06-25 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0005_chat_box'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('current_date', models.DateField()),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
            ],
        ),
        migrations.DeleteModel(
            name='Chat_box',
        ),
    ]