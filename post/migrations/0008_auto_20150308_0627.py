# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(related_name='posts', verbose_name=b'List of Authors', to='author.Author'),
            preserve_default=True,
        ),
    ]
