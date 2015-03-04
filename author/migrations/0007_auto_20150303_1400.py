# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_auto_20150303_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
