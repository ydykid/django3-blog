# from django.db import models
from django.contrib.auth import get_user_model
# from django_extensions.db import models as m

# Create your models here

User = get_user_model()

# class Model(m.TimeStampedModel):
#
#     created_user = models.ForeignKey(User,
#                                      verbose_name='创建人',
#                                      help_text='创建人',
#                                      on_delete=models.SET_NULL,
#                                      null=True,
#                                      blank=True)
#
#     modified_user = models.ForeignKey(User,
#                                       verbose_name='修改人',
#                                       help_text='修改人',
#                                       on_delete=models.SET_NULL,
#                                       null=True,
#                                       blank=True)
