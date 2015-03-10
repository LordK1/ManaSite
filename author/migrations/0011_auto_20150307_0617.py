# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0010_auto_20150304_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
