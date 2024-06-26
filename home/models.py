from datetime import datetime
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from modeltrans.fields import TranslationField
from django.contrib.postgres.indexes import GinIndex


class AboutMe(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.DateField()
    nationality = models.CharField(max_length=10)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    image = models.ImageField(upload_to='covers/user_me')

    bio = models.CharField(max_length=200)
    description = RichTextField()

    i18n = TranslationField(fields=('name', 'last_name', 'nationality', 'bio', 'description'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]
        verbose_name_plural = "About Me"

    def get_age_year(self):
        return datetime.now().year - self.age.year

    def __str__(self):
        return f'{self.name} {self.last_name}'


