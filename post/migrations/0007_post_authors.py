# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0011_auto_20150307_0617'),
        ('post', '0006_auto_20150302_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(related_name='posts', to='author.Author'),
            preserve_default=True,
        ),
    ]
