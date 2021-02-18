from django import forms
from user.models import User


class UpdateStatus(forms.ModelForm):
    class Meta:
        model = User
        fields = ('status',)