from django import forms
from .models import Acta

class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta
        fields = {
            'fechaActa',
            'numActa',
            'copActa',
        }