#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/26 23:01|23:01
# @Author  : yangdingyi
# @File    : adminx
# @Software: PyCharm

import xadmin
from xadmin import views


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'ydy后台'
    site_footer = 'ydy'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
