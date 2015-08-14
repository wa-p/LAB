from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.template import loader

import datetime

from forms import SolicitudForm
from forms import RegistroForm

from django.contrib.auth.models import User
from models import Estatus_Solicitud, Solicitud

@login_required
def home(request):
   usuario = User.objects.get(id=request.user.id)
   request.session['usuario'] = usuario.first_name
   solicituds = Solicitud.objects.filter(ci=usuario).order_by('estatus_Solicitud', 'fecha_creacion')
   t = loader.get_template('../templates/index.html')
   c = RequestContext(request, {'solicituds' : solicituds})
   return HttpResponse(t.render(c))

@login_required
def crear_solicitud(request):
    if request.POST:
        form = SolicitudForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            usuario = User.objects.get(id=request.user.id)
            registro.ci = User.objects.get(id=usuario.id)
            registro.fecha_creacion = datetime.datetime.now()
            registro.estatus_solicitud = Estatus_Solicitud.objects.get(id=1)
            registro.fecha_estimada='2020-01-01'
            registro.save()

            return HttpResponseRedirect('/solicituds')
    else:
        form = SolicitudForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('crear_solicitud.html', args)

@login_required
def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(solicitud, id=id)
    solicitud.delete()
    return HttpResponseRedirect('/solicituds')

@login_required
def actualizar_estatus(request, id):
    solicitud = get_object_or_404(solicitud, id=id)
    if solicitud.estatus_solicitud.id == 1:
        solicitud.estatus_solicitud = Estatus_solicitud.objects.get(id=2)
        solicitud.save()
        return HttpResponseRedirect('/solicituds')
    else:
        solicitud.estatus_solicitud = Estatus_solicitud.objects.get(id=1)
        solicitud.save()
        return HttpResponseRedirect('/solicituds')

@login_required
def ver_solicitud(request, id):    
    solicitud = get_object_or_404(solicitud, id=id)
    return render_to_response('ver_solicitud.html', {'solicitud' : solicitud})

@login_required
def logout(request): 
    request.session['usuario'] = ' ' 
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login.html")

#def registro(request):
 #   return render_to_response('registro.html')

def registro(request):
    if request.POST:
        form = RegistroForm(request.POST)
        if form.is_valid():
            datos = registro = form.save(commit=False)
            usuario= User.objects.create_user(datos.username, datos.email, datos.password)
            usuario.ci=datos.name
            usuario.last_name=datos.last_name
            usuario.save();
            return HttpResponseRedirect("/login")
    else:
        form = RegistroForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registro.html', args)


@login_required
def ver_status(request):
   usuario = User.objects.get(id=request.user.id)
   request.session['usuario'] = usuario.last_name
   solicituds = Solicitud.objects.filter(ci=usuario).order_by('estatus_solicitud', 'fecha_creacion')
   t = loader.get_template('../templates/ver_status.html')
   c = RequestContext(request, {'solicituds' : solicituds})
   return HttpResponse(t.render(c))