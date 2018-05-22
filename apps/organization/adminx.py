# _*_ encoding:utf-8 _*_
__author__ = "king"
__date__ = "2018/5/22 下午11:01"

import xadmin

from .models import CityDict, Teacher, CourseOrg


class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]


class TeacherAdmin(object):
    list_display = ["org", "name", "work_years", "work_company", "work_position", "click_nums",
                    "fav_nums", "age", "image", "add_time"]
    search_fields = ["org", "name", "work_years", "work_company", "work_position", "click_nums",
                     "fav_nums", "age", "image"]
    list_filter = ["org", "name", "work_years", "work_company", "work_position", "click_nums",
                   "fav_nums", "age", "image", "add_time"]


class CourseOrgAdmin(object):
    list_display = ["name", "desc", "tag", "category", "click_nums", "fav_nums", "image", "address",
                    "city", "students", "course_nums", "add_time"]
    search_fields = ["name", "desc", "tag", "category", "click_nums", "fav_nums", "image", "address",
                     "city", "students", "course_nums"]
    list_filter = ["name", "desc", "tag", "category", "click_nums", "fav_nums", "image", "address",
                   "city", "students", "course_nums", "add_time"]
    pass


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
