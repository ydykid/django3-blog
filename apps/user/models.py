from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractUser):

    name = models.CharField(_("Name of User"),
                            blank=True,
                            max_length=255
                            )

    class Meta:
        verbose_name = '账户'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})
