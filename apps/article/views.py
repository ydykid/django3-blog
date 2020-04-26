# from django.shortcuts import render
from rest_framework import (
    viewsets, mixins,
)

from .serializers import ArticleSerializer

from .models import Article

# Create your views here.


class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


