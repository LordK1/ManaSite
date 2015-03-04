# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_author_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
    ]
