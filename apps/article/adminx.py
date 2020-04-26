#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:14|00:14
# @Author  : yangdingyi
# @File    : adminx
# @Software: PyCharm

from .models import Article
import xadmin


class ArticleAdmin(object):
    pass


xadmin.site.register(Article, ArticleAdmin)

