from django import forms

from .models import Inst

class InstForm(forms.ModelForm):

    class Meta:
        model = Inst
        fields = ('email', 'password',)