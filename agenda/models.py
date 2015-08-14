from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 7)
    ci= models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
    	return self.username

class Estatus_Solicitud(models.Model):
	descripcion = models.TextField()

	def __str__(self):
		return self.descripcion


class Tipo_Solicitud(models.Model):
	descripcion = models.TextField()

	def __str__(self):
		return self.descripcion

class Materia(models.Model):
	codigo = models.IntegerField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	escuela = models.CharField(max_length = 30)
	capacidad = models.IntegerField()
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


class Solicitud(models.Model):
	cod_solicitud = models.AutoField(primary_key=True)
	ci = models.ForeignKey(User)
	estatus_solicitud = models.ForeignKey(Estatus_Solicitud)
	fecha_creacion = models.DateField()
	fecha_estimada = models.DateField()
	materia = models.ForeignKey(Materia)
	tipo_solicitud = models.ForeignKey(Tipo_Solicitud)
	kardex =  models.CharField(max_length = 30, default='/home')
	carta_explicativa =  models.CharField(max_length = 30, default='/home')



	def __str__(self):
		return self.tipo_solicitud

