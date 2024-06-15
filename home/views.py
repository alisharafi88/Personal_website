from django.shortcuts import render, get_object_or_404
from django.views import generic, View



class HomeView(View):
    def get(self, request):
        return render(request, '-base.html')


