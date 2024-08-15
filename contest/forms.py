from django.forms import ModelForm
from .models import Participant

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ('name', 'email', 'code')
