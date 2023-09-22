from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('profile', 'email')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput({'placeholder': 'Whats Your Name?!'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput({'placeholder': 'Enter Your Password?!'}))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
