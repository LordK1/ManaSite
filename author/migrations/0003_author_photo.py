# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to=b'users'),
            preserve_default=False,
        ),
    ]
