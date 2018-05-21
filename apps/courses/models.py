# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organization.models import CourseOrg


# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情", default="")
    is_banner = models.BooleanField(verbose_name=u"是否轮播图", default=False)
    degree = models.CharField(verbose_name=u"课程难度级别", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")),max_length=10)
    learn_time = models.IntegerField(verbose_name=u"学习时长(分钟)", default=0)
    students = models.IntegerField(verbose_name=u"学生人数", default=0)
    fav_num = models.IntegerField(verbose_name=u"收藏人数", default=0)
    image = models.ImageField(verbose_name=u"封面图", max_length=200, upload_to="course/%Y/%m")
    click_name = models.ImageField(verbose_name=u"课程点击数", default=0)
    category = models.CharField(verbose_name=u"课程类别", max_length=30, default=u"后端开发")
    tag = models.CharField(verbose_name=u"课程的标签", max_length=30)

    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=50, verbose_name=u"章节名")
    learn_time = models.IntegerField(verbose_name=u"学习时长(分钟)", default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名字")
    learn_time = models.IntegerField(verbose_name=u"学习时长(分钟)", default=0)
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(max_length=100, upload_to="course/resource/%Y/%m", verbose_name=u"课程资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name








