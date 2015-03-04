# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='create_date',
            field=models.DateTimeField(default=datetime.now(), auto_now_add=True),
            preserve_default=False,
        ),
    ]
