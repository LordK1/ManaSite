# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0008_auto_20150304_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(upload_to=b'users'),
            preserve_default=True,
        ),
    ]
