# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20171031_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '章节', 'verbose_name_plural': '章节'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '视频', 'verbose_name_plural': '视频'},
        ),
    ]