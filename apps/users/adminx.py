import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    """全站的设置放在用户应用的adminx中,建立一个BaseSetting(object)"""
    enable_themes = True
    use_bootswatch = True

class GlobalSeetings(object):
    site_title = '跟Peter一起学python'
    site_footer = '波波在线'
    menu_style = 'accordion'



class EmailVerifyRecordAdmin(object):
    list_diplay = ['id', 'code', 'email', 'send_type', 'send_time']
    list_filter = ['id', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_per_page = 5


class BannerAdmin(object):

    list_diplay = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'index', 'add_time']
    list_per_page = 5


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
#　将主题功能注册进来
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSeetings)