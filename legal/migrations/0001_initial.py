# Generated by Django 5.0.6 on 2024-06-27 14:13

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipc_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=25, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('punishment', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('usertype', models.CharField(max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Advocate_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('gender', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('advocate_type', models.CharField(max_length=25, null=True)),
                ('id_proof', models.FileField(null=True, upload_to='')),
                ('degree_cerificate', models.FileField(null=True, upload_to='')),
                ('licence', models.FileField(null=True, upload_to='')),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('approved', models.BooleanField(default=False)),
                ('login_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('posted_date', models.DateField(null=True)),
                ('accepted_date_user', models.DateField(null=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Request_work_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, null=True)),
                ('approval', models.BooleanField(default=False, null=True)),
                ('accepted_date', models.DateField(null=True)),
                ('accepted_date_user', models.DateField(null=True)),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
                ('case_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.cases')),
            ],
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('gender', models.CharField(max_length=25, null=True)),
                ('id_proof', models.FileField(null=True, upload_to='')),
                ('profile_picture', models.ImageField(null=True, upload_to='')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('login_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('current_date', models.DateField(null=True)),
                ('accepted_date', models.DateField(null=True)),
                ('status', models.BooleanField(null=True)),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('posted_date', models.DateField()),
                ('advocate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.advocate_registration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration')),
            ],
        ),
        migrations.AddField(
            model_name='cases',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legal.user_registration'),
        ),
    ]
