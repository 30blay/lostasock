from django import forms
from .models import Sock


class SockForm(forms.ModelForm):
    class Meta:
        model = Sock
        fields = ('image',)