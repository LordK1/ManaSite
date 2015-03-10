# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0014_auto_20150309_0808'),
        ('post', '0008_auto_20150308_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(related_name='followed', to='author.Author')),
                ('follower', models.ForeignKey(related_name='follower', to='author.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='likes', to='author.Author')),
                ('post', models.ForeignKey(related_name='likes', to='post.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
