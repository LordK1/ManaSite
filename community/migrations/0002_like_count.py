# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
