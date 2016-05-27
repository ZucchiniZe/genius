# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 21:47
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('peak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peak',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
