#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2020/4/27 00:25|00:25
# @Author  : yangdingyi
# @File    : serializers
# @Software: PyCharm
from django.contrib.auth import get_user_model
from rest_framework import serializers

from my_base import serializers as base_serializers
from .models import (
    Article,
    Comment, CommentArticleUserRel, Tag,
)

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(base_serializers.BaseModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CommentArticleUserRelSerializer(serializers.ModelSerializer):

    # content = serializers.CharField(read_only=True)

    class Meta:
        model = CommentArticleUserRel
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    comment_m2m = UserSerializer(many=True,)

    comment_m2m_method = serializers.SerializerMethodField()

    def get_comment_m2m_method(self, obj):
        comments = CommentArticleUserRel.objects.filter(article=obj)
        return CommentArticleUserRelSerializer(
            comments, many=True, context=self.context).data

    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleIdsSerializer(base_serializers.BaseNoSaveSerializer):

    # ids = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=Article.objects.all()),
    #                                  )
    ids = serializers.ListSerializer(
        required=False,
        child=serializers.IntegerField())




