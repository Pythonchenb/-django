from django.db import models
from datetime import datetime

class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name='城市')
    desc = models.CharField(max_length=200,verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourceOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name='机构名称')
    desc = models.TextField('机构描述')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m',verbose_name='封面图')
    address = models.CharField(max_length=50,verbose_name='机构地址')
    city = models.ForeignKey(CityDict,verbose_name='所在城市')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourceOrg,verbose_name='所属机构')
    name = models.CharField(max_length=20,verbose_name='教师名')
    work_years = models.IntegerField(default=0,verbose_name='工作年限')
    work_company = models.CharField(max_length=50,verbose_name='公司')
    work_position = models.CharField(max_length=50,verbose_name='工作职位')
    points = models.CharField(max_length=50,verbose_name='教学风格')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')


    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name