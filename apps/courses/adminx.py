# _*_ encoding:utf-8 _*_
__author__ = "king"
__date__ = "2018/5/22 下午10:45"

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "is_banner", "degree", "learn_time",
                    "students", "fav_num", "image", "click_name", "category", "tag", "add_time"
                    ]
    search_fields = ["name", "desc", "detail", "is_banner", "degree", "learn_time",
                     "students", "fav_num", "image", "click_name", "category", "tag"
                     ]
    list_filter = ["name", "desc", "detail", "is_banner", "degree", "learn_time",
                   "students", "fav_num", "image", "click_name", "category", "tag", "add_time"
                   ]


class LessonAdmin(object):
    list_display = ["course", "name", "learn_time", "add_time"]
    search_fields = ["course", "name", "learn_time"]
    list_filter = ["course", "name", "learn_time", "add_time"]


class VideoAdmin(object):
    list_display = ["lesson", "name", "learn_time", "url", "add_time"]
    search_fields = ["lesson", "name", "learn_time", "url"]
    list_filter = ["lesson", "name", "learn_time", "url", "add_time"]


class CourseResourceAdmin(object):
    list_display = ["course", "name", "download", "add_time"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course", "name", "download", "add_time"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
