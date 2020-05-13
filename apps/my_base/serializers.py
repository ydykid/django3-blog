#!/usr/env/bin python
# -*- coding: utf-8 -*-

# @Time    : 2019/6/18 16:34
# @Author  : yangdy
# @Email   : yangdy@egu360.com
# @File    : serializers.py
# @Software: PyCharm

__author__ = 'yangdy'


from rest_framework.serializers import ModelSerializer, Serializer


class CreatedUserSerializer(ModelSerializer):
    """
    created user
    """
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_user'] = user
        validated_data['modified_user'] = user
        return super(CreatedUserSerializer, self).create(validated_data)


class ModifiedUserSerializer(ModelSerializer):
    """
    modified user
    """
    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['modified_user'] = user
        return super(ModifiedUserSerializer, self).update(instance, validated_data)


class CreatedModifiedUserSerializer(ModelSerializer):
    """
    created modified user
    """
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_user'] = user
        validated_data['modified_user'] = user
        return super(CreatedModifiedUserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['modified_user'] = user
        return super(CreatedModifiedUserSerializer, self).update(instance, validated_data)


class BaseNoSaveSerializer(Serializer):

    @property
    def object(self):
        return self.validated_data

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BaseModelSerializer(ModelSerializer):

    @property
    def object(self):
        return self.validated_data
