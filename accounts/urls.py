from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('singup/', views.UserRegisterView.as_view(), name='singup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
