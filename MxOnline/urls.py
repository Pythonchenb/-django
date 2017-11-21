"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from orgnization.views import OrgView
from users.views import LoginView,RegisterView, ActiveUserView,ForgetPwdView, ResetView, ModifyPwdView

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$',ForgetPwdView.as_view(),name='forgetpwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$',ModifyPwdView.as_view(),name='modify_pwd'),
    # 组织机构页面
    url(r"^org/",include('orgnization.urls',namespace ='org')),
]
