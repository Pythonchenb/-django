# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courceorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default=0, max_length=20, verbose_name='机构类别'),
        ),
    ]
