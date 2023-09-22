from datetime import datetime
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from modeltrans.fields import TranslationField
from django.contrib.postgres.indexes import GinIndex


class Me(models.Model):

    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.DateField()
    nationality = models.CharField(max_length=10)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    image = models.ImageField(upload_to='covers/user_me')

    summery_text = models.CharField(max_length=200)
    text = RichTextField()

    i18n = TranslationField(fields=('name', 'last_name', 'nationality', 'summery_text', 'text'))

    class Meta:
        indexes = [GinIndex(fields=["i18n"])]

    def get_age_year(self):
        return datetime.now().year - self.age.year

    def __str__(self):
        return f'{self.name} {self.last_name}'


class File(models.Model):
    user = models.OneToOneField(Me, on_delete=models.CASCADE, related_name='file')
    image_name = models.CharField(max_length=5)
    File = models.FileField(upload_to='covers/user_me')

    def __str__(self):
        return f'{self.user.name} {self.user.last_name}`s file'
