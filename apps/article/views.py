# from django.shortcuts import render
from rest_framework import (
    viewsets, mixins, status,
)
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    ArticleSerializer,
    ArticleDetailSerializer,
    ArticleIdsSerializer,
)

from .models import Article

# Create your views here.


class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        if self.action == 'ids':
            return ArticleIdsSerializer
        elif self.action == 'list':
            return ArticleDetailSerializer
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleSerializer

    @action(methods=['post'], detail=True)
    def ids(self, request, pk=id):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ids = serializer.object.get('ids')
            return Response({'ids': ids})

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

