#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:14|00:14
# @Author  : yangdingyi
# @File    : adminx
# @Software: PyCharm

import xadmin

from .models import (
    Article, Category, Tag,
    Comment, CommentArticleUserRel,
)


class CategoryAdmin(object):
    pass


class TagAdmin(object):
    pass


class ArticleAdmin(object):
    list_display = ['title', 'category', 'tags']
    style_fields = {
        # 'tags': 'm2m_transfer',
        'tags': 'm2m_dropdown',
        'comment_m2m': 'm2m_transfer',
        # 'comment_m2m': 'm2m_dropdown'
    }

    class CommentItemInline(object):
        model = Comment
        style = 'tab'
        ordering = ('-created',)
        extra = 1

    class CommentArticleUserRelInline(object):
        model = CommentArticleUserRel
        style = 'tab'
        extra = 1

    inlines = [CommentItemInline, CommentArticleUserRelInline]


class CommentAdmin(object):
    pass


class CommentArticleUserRelAdmin(object):
    pass


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(CommentArticleUserRel, CommentArticleUserRelAdmin)

