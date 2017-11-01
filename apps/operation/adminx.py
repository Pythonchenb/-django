import xadmin
from operation.models import UserAsk, CourseConment, UserMessage, UserFavorite, UserCourse


class UserAskAdmin(object):

    list_display = ['name','mobile','course_name','add_time']
    list_filter = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name','add_time']
    list_per_page =5


class CourseConmentAdmin(object):

    list_display = ['user', 'course', 'conments', 'add_time']
    list_filter = ['user', 'course', 'conments', 'add_time']
    search_fields = ['user', 'course', 'conments']
    list_per_page = 5



class UserMessageAdmin(object):

    list_display = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_per_page = 5

class UserFavoriteAdmin(object):

    list_display = ['fav_id', 'fav_type', 'add_time']
    list_filter = ['fav_id', 'fav_type', 'add_time']
    search_fields = ['fav_id', 'fav_type']
    list_per_page = 5


class UserCourseAdmin(object):

    list_display = ['user', 'course', 'add_time']
    list_filter = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_per_page = 5

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseConment,CourseConmentAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)