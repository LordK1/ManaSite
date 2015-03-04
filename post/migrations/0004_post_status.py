# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20150302_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default='A', max_length=1, choices=[(b'A', b'Active'), (b'P', b'Pending'), (b'D', b'De Active')]),
            preserve_default=False,
        ),
    ]
