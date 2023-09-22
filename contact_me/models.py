from django.db import models


class ContactMe(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    seen = models.BooleanField(default=False, blank=True, null=True)
    message_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.subject}'
