from django.conf.urls import include,url

from orgnization.views import OrgView, UserAskView

urlpatterns = [
    # 课程机构
    url(r'^org_list/$', OrgView.as_view(), name='org_list'),
    url(r'^user_ask/$', UserAskView.as_view()),
]
