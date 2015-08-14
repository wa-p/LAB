from django import forms
from models import Estatus_Solicitud
from models import Solicitud
from models import Usuario

from django.contrib.auth.models import User

class SolicitudForm(forms.ModelForm):
 
   class Meta:
      model = Solicitud
      fields = ('tipo_solicitud','kardex','carta_explicativa', 'materia')
      exclude = ('ci','fecha_creacion')

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('username','password', 'email','ci', 'last_name')
		#exclude = ('name', 'last_name')
