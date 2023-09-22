from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Me as mee


def me(request):
    me = get_object_or_404(mee, pk=1)
    return {'me': me}
