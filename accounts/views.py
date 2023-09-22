from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .forms import CustomUserCreationForm, UserLoginForm


class UserRegisterView(View):
    form_class = CustomUserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _(f'{request.user.username}, You are authenticated!'), 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/singup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _('Now Login'), 'success')
            return redirect('account:login')
        messages.error(request, _('Try again!'), 'danger')
        return render(request, 'accounts/singup.html')


class UserLoginView(View):
    form_class = UserLoginForm

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _(f'{request.user.username}, You are authenticated!'), 'warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, _('You Logged in'), 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
        messages.error(request, _('Try again!'), 'danger')
        return render(request, 'accounts/login.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, _('You Logged out!'), 'success')
        return redirect('home:home')
