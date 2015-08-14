from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin

urlpatterns = patterns('agenda.views',
    # Examples:
    # url(r'^$', 'Gestor_solicituds.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^solicituds/', 'home', name='home'),
    url(r'^crear_solicitud/$', 'crear_solicitud', name='crear_solicitud'),
	url(r'^ver_solicitud/(?P<id>[\w ]+)/$', 'ver_solicitud', name = 'ver_solicitud'),
	url(r'^eliminar_solicitud/(?P<id>[\w ]+)/$', 'eliminar_solicitud', name = 'eliminar_solicitud'),
    url(r'^actualizar_estatus/(?P<id>[\w ]+)/$', 'actualizar_estatus', name = 'actualizar_estatus'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'logout.html', }, name="logout"),
    url(r'^registro/', 'registro', name='registro'),
    url(r'^ver_status/', 'ver_status', name='ver_status'),

)
