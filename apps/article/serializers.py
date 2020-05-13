#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:25|00:25
# @Author  : yangdingyi
# @File    : serializers
# @Software: PyCharm

from rest_framework import serializers

from my_base import serializers as base_serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleIdsSerializer(base_serializers.BaseNoSaveSerializer):

    # ids = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=Article.objects.all()),
    #                                  )
    ids = serializers.ListSerializer(
        required=False,
        child=serializers.IntegerField())




