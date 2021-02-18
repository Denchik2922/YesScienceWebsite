from django.shortcuts import render
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


class UserLoginView(LoginView):
    form_class = AuthUserForm
    template_name = 'user_page/login_form.html'
    success_url = reverse_lazy('list_article_url')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('list_article_url')


class UserRegisterView(CreateView):
    model = User
    template_name = 'user_page/register_form.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('list_article_url')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid
