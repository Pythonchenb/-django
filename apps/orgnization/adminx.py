import xadmin
from orgnization.models import CityDict, CourceOrg, Teacher


class CityDictAdmin(object):
    list_diplay = ['name', 'desc', 'add_time']

    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_per_page = 5


class CourceOrgAdmin(object):
    list_diplay = ['name', 'desc', 'click_nums', 'fav_nums',
                   'image', 'address', 'city']

    list_filter = ['name', 'desc', 'click_nums', 'fav_nums',
                   'image', 'address', 'city']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums',
                     'image', 'address', 'city']
    list_per_page = 5


class TeacherAdmin(object):
    list_diplay = ['org', 'name', 'work_years', 'work_company',
                   'work_position', 'points', 'click_nums', 'fav_nums']

    list_filter = ['org', 'name', 'work_years', 'work_company',
                   'work_position', 'points', 'click_nums', 'fav_nums']

    search_fields = ['org', 'name', 'work_years', 'work_company',
                     'work_position', 'points', 'click_nums', 'fav_nums']
    list_per_page = 5


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourceOrg, CourceOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
