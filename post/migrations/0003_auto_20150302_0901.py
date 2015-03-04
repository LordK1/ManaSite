# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150302_0851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=datetime.datetime(2015, 3, 2, 9, 1, 45, 837617, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
