from django.contrib import admin
from models import Estatus_Solicitud
from models import Solicitud
from models import Tipo_Solicitud
from models import Materia
 
admin.site.register(Estatus_Solicitud)
admin.site.register(Solicitud)
admin.site.register(Tipo_Solicitud)
admin.site.register(Materia)