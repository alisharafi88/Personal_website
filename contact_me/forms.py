from django import forms

from .models import ContactMe


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
