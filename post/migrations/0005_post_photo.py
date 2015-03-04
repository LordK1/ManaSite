# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to=b'/home/k1/Workspaces/PycharmProjects/ManaSite/media/photos'),
            preserve_default=False,
        ),
    ]
