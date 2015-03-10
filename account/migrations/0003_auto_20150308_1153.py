# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('account', '0002_auto_20150308_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='birthdate',
            new_name='birthday',
        ),
        migrations.AddField(
            model_name='account',
            name='biography',
            field=models.CharField(max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 8, 11, 52, 41, 131261, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='sample@email.com', unique=True, max_length=255, verbose_name=b'email address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(default='male', max_length=1, choices=[(b'male', b'Male'), (b'female', b'Female')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='', unique=True, max_length=20, validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]', message=b'Only numeric characters are allowed !!!')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default=b'/static/images/13.jpg', upload_to=b'accounts'),
            preserve_default=True,
        ),
    ]
