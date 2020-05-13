from rest_framework.permissions import BasePermission
from django.db.models import Q

from user.models import Role


class IsContestant(BasePermission):
    """
    项目参赛者权限
    """

    def has_permission(self, request, view):
        # if not bool(request.user and request.user.is_authenticated):
        #     return False
        # try:
        #     role = Role.objects.filter(remark='contestant')[0]
        #     return bool(role in request.user.user_info.roles.all())
        # except Exception:
        #     return False
        return bool(request.user and request.user.is_authenticated)


class IsCheckerOrAdmin(BasePermission):
    """
    大赛审核员权限
    """

    def has_permission(self, request, view):
        # if not bool(request.user and request.user.is_authenticated):
        #     return False
        # try:
        #     roles = Role.objects.filter(Q(remark='checker') | Q(remark='admin'))
        #     for role in roles:
        #         if bool(role in request.user.user_info.roles.all()):
        #             return True
        #     return False
        # except Exception:
        #     return False
        return bool(request.user and request.user.is_authenticated)


class IsWebsiteOrAdmin(BasePermission):
    """
    官网管理员权限
    """

    def has_permission(self, request, view):
        # if not bool(request.user and request.user.is_authenticated):
        #     return False
        # try:
        #     roles = Role.objects.filter(Q(remark='website') | Q(remark='admin'))
        #     for role in roles:
        #         if bool(role in request.user.user_info.roles.all()):
        #             return True
        #     return False
        # except Exception:
        #     return False
        return bool(request.user and request.user.is_authenticated)


class IsAdmin(BasePermission):
    """
    大赛审核员权限
    """

    def has_permission(self, request, view):
        # if not bool(request.user and request.user.is_authenticated):
        #     return False
        # try:
        #     role = Role.objects.filter(remark='admin')[0]
        #     return bool(role in request.user.user_info.roles.all())
        # except Exception:
        #     return False
        return bool(request.user and request.user.is_authenticated)
