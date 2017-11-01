import xadmin
from .models import Course, Lesson, Video, CourseResouce


class CourseAdmin(object):

    list_diplay = ['name', 'desc', 'detail', 'degree', 'times',
                   'students','fav_nums','image','click_nums','add_time']

    list_filter = ['name', 'desc', 'detail', 'degree', 'times',
                   'students','fav_nums','image','click_nums','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'times',
                   'students','fav_nums','image','click_nums']
    list_per_page = 5

class LessonAdmin(object):

    list_diplay = ['course','name', 'add_time' ]

    list_filter = ['course__name','name', 'add_time' ]
    search_fields = ['course','name']
    list_per_page = 5

class VideoAdmin(object):

    list_diplay = ['lesson', 'name', 'add_time']

    list_filter = ['lesson__name', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_per_page = 5

class CourseResouceAdmin(object):
    """
    course = models.ForeignKey('Course',verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name='资源文件',max_length=100)
    add_time
    """
    list_diplay = ['course', 'name', 'download','add_time']

    list_filter = ['course__name', 'name', 'download','add_time']
    search_fields = ['course', 'name', 'download']
    list_per_page = 5



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResouce,CourseResouceAdmin)

