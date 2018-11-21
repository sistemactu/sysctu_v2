from django import forms
from .models import Socio


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = (
            'nombCompSoc',
            'rutSoc',
            'domicSoc',
            'fecNacSoc',
            'mailSoc',
            'celSoc',
            'telSoc',
            'profecSoc',
            'trabSoc',
            'edadSoc',
            'nacionalidadSoc',
            'estCivSoc',
            'conySoc',
            'numHijMenSoc',
            'poctSoc',
            'ocsSoc',
            'catTenSoc',
            'numCas',
            'cuotInc',
            'cuotSoc',
            'totPag',
            'formPaInsc',
            'tipoSoc',
            'socPatr',
            'primSocFe',
            'secSocFe',
            'fecSolic',
            'estSolic',
            'acta',
            'fecAcept',
            'infSolic',
            'fotoSoc',
        )

