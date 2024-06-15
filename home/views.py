from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import AboutMe


class HomeView(View):
    def get(self, request):
        about_me = get_object_or_404(AboutMe, pk=1)
        return render(request, '-base.html', {'about_me': about_me})

