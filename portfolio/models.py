from django.db import models

from django.contrib.postgres.indexes import GinIndex
from ckeditor.fields import RichTextField
from modeltrans.fields import TranslationField


class Portfolio(models.Model):
    category = models.CharField(max_length=30)
    client = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    description = RichTextField(blank=True, null=True)
    cover = models.ImageField(upload_to='portfolio')

    i18n = TranslationField(fields=('category', 'description'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]

    def __str__(self):
        return self.category


class ImgForPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='img')
    img = models.ImageField(upload_to='covers/portfolio/%Y/%m')


class LinkForPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='links')
    link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True,
    )

    def __str__(self):
        return self.link
