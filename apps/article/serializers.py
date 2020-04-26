#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:25|00:25
# @Author  : yangdingyi
# @File    : serializers
# @Software: PyCharm

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
