from django import forms
from django.forms import ModelForm
from .models import Participant

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ('name', 'email', 'code')
        labels = {
            'name': '',
            'email': '',
            'code': '',
        }
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                'code': forms.Textarea(attrs={'placeholder': 'Code', 'class': 'form-control'}),
            }
