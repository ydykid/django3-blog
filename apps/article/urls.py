#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:26|00:26
# @Author  : yangdingyi
# @File    : urls
# @Software: PyCharm

from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet

router = DefaultRouter()

router.register(r'article',
                ArticleViewSet,
                basename='api/article')

app_name = 'article'

urlpatterns = []

urlpatterns += router.urls

