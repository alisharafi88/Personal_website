from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import ContactMeForm


def get_message(request):
    form = ContactMeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, _('Your message has been received'), 'success')
        return redirect('home:home')
    messages.error(request, _('Something wrong happened. Try again!'), 'warning')
    return redirect('home:home')
