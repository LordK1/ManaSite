# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_like_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='count',
            new_name='numerator',
        ),
    ]
