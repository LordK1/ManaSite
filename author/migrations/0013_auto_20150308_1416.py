# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0012_auto_20150308_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_post_publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 8, 14, 16, 31, 819252, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='post_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='account',
            field=models.OneToOneField(related_name='author', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
