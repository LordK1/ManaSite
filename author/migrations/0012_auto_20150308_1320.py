# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0011_auto_20150307_0617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='author',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
    ]
