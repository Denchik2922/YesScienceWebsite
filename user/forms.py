from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django import forms


class AuthUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.status = 'Новичек'
        if commit:
            user.save()
        return user