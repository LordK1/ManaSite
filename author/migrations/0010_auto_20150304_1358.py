# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0009_auto_20150304_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'users'),
            preserve_default=True,
        ),
    ]
