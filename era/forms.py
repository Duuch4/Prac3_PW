from django.forms import ModelForm
from era.models import Facultad, Carrera

class FacultadForm(ModelForm):
    class Meta:
        model = Facultad
        exclude = ('user', 'date',)

class CarrerForm(ModelForm):
    class Meta:
        model = Carrera
        exclude = ('user', 'date', 'Facultad_idFacultad',)