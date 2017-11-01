# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='城市')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='CourceOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.TextField(verbose_name='机构描述')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏数', default=0)),
                ('image', models.ImageField(verbose_name='封面图', upload_to='org/%Y/%m')),
                ('address', models.CharField(max_length=50, verbose_name='机构地址')),
                ('city', models.ForeignKey(verbose_name='所在城市', to='orgnization.CityDict')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='教师名')),
                ('work_years', models.IntegerField(verbose_name='工作年限', default=0)),
                ('work_company', models.CharField(max_length=50, verbose_name='公司')),
                ('work_position', models.CharField(max_length=50, verbose_name='工作职位')),
                ('points', models.CharField(max_length=50, verbose_name='教学风格')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏数', default=0)),
                ('org', models.ForeignKey(verbose_name='所属机构', to='orgnization.CourceOrg')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
