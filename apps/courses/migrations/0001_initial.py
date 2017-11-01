# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(max_length=2, choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')])),
                ('times', models.IntegerField(verbose_name='学习时候长(分钟数)', default=0)),
                ('students', models.IntegerField(verbose_name='学习人数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏人数', default=0)),
                ('image', models.ImageField(verbose_name='封面', upload_to='course/%Y/%m')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseResouce',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('download', models.FileField(verbose_name='资源文件', upload_to='course/resource/%Y/%m')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('course', models.ForeignKey(verbose_name='课程', to='courses.Course')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='课程名')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('course', models.ForeignKey(verbose_name='课程', to='courses.Course')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('lesson', models.ForeignKey(verbose_name='章节', to='courses.Lesson')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
    ]
