from django.db import models

from modeltrans.fields import TranslationField
from ckeditor.fields import RichTextField


class Blog(models.Model):
    subject = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    body = RichTextField()
    cover = models.ImageField(upload_to='covers/blogs/%y/%m', null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    i18n = TranslationField(fields=('subject', 'title', 'body'))
