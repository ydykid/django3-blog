from django.db import models
from django_extensions.db import models as m

from ckeditor.fields import RichTextField
# Create your models here.


class Article(m.TimeStampedModel):
    title = models.CharField(verbose_name='标题',
                             max_length=255)

    content = RichTextField(verbose_name='内容',
                            max_length=1500)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

