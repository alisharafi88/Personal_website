from django.db import models
from django.utils.translation import gettext as _

from accounts.models import CustomUser


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='testimonials',
        verbose_name=_('User'),
    )
    comment = models.CharField(max_length=300)

    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
