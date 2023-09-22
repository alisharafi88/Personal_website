from django.urls import path

from .views import get_message

app_name = 'contact_me'
urlpatterns = [
    path('', get_message, name='message')
]
