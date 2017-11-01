# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171025_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='female', max_length=1, choices=[('male', '男'), ('female', '女')]),
        ),
    ]
