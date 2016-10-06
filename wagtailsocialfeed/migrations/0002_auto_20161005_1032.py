# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsocialfeed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialfeedpage',
            name='feedconfig',
            field=models.ForeignKey(blank=True, help_text='Leave blank to show all the feeds.', null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailsocialfeed.SocialFeedConfiguration'),
        ),
    ]