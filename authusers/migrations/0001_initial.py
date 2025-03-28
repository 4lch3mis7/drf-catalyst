# Generated by Django 5.1.4 on 2025-01-12 00:27

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('role', models.CharField(choices=[('SU', 'Super User'), ('AD', 'Admin'), ('UR', 'User')], default='UR', max_length=2)),
                ('is_active', models.BooleanField(default=False, help_text='Inactive users can not log into the system.')),
                ('is_staff', models.BooleanField(default=False, help_text='staffs can access django admin panel with assigned permissions.')),
                ('is_superuser', models.BooleanField(default=False)),
                ('deletion_initiated_at', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile-picture/')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='NP', unique=True)),
            ],
        ),
    ]
