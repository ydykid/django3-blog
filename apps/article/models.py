# -*- coding:utf-8 -*-
import logging

from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db import models as m

from ckeditor.fields import RichTextField


# Create your models here.
logger = logging.getLogger(__name__)
User = get_user_model()


class Category(m.TimeStampedModel):
    """
    Article Category
    """
    name = models.CharField(verbose_name='类别名称',
                            help_text='类别名称',
                            max_length=50)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(m.TimeStampedModel):
    """
    Article Tag
    """

    name = models.CharField(verbose_name='标签名称',
                            help_text='标签名称',
                            max_length=50)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(m.TimeStampedModel):
    title = models.CharField(verbose_name='标题',
                             help_text='标题',
                             max_length=255)

    category = models.ForeignKey(Category,
                                 verbose_name='类别',
                                 help_text='类别',
                                 related_name='articles',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    tags = models.ManyToManyField(Tag,
                                  verbose_name='标签',
                                  help_text='标签',
                                  related_name='articles',
                                  )

    content = RichTextField(verbose_name='内容',
                            help_text='内容',
                            max_length=1500)

    comment_m2m = models.ManyToManyField(User,
                                         verbose_name='评论(m2m)',
                                         help_text='评论(m2m)',
                                         through='CommentArticleUserRel',
                                         through_fields=('article', 'user'),
                                         related_name='comment_m2m_articles',
                                         )

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class CommentArticleUserRel(m.TimeStampedModel):
    article = models.ForeignKey(Article,
                                related_name='comments',
                                on_delete=models.CASCADE,
                                )
    user = models.ForeignKey(User,
                             related_name='article_comments',
                             on_delete=models.CASCADE,
                             )
    content = models.TextField(verbose_name='评论(m2m)',
                               help_text='评论(m2m)',
                               )

    class Meta:
        verbose_name = '评论(article2user)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.article}|{self.user}(m2m)'


class Comment(m.TimeStampedModel):

    article = models.ForeignKey(Article,
                                verbose_name='文章',
                                help_text='文章',
                                on_delete=models.CASCADE)

    user = models.ForeignKey(User,
                             verbose_name='用户',
                             help_text='用户',
                             on_delete=models.CASCADE)

    content = models.TextField(verbose_name='评论',
                               help_text='评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return f'{self.article}|{self.user}'
