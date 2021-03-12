from django import forms
from .models import signup, mynotes

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class mynotesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'