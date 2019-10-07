from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/paciente/paciente/(?P<pk>[0-9]+)$', # Url to get update or delete a paciente
        views.get_delete_update_paciente.as_view(), 
        name='get_delete_update_paciente'
    ),
    path('api/v1/paciente/paciente', # urls list all and create new paciente
        views.get_post_pacientes.as_view(),
        name='get_post_pacientes'
    ),
    re_path(r'^api/v1/paciente/expediente/(?P<pk>[0-9]+)$', # Url to get update or delete a expediente
        views.get_delete_update_expediente.as_view(),
        name='get_delete_update_expediente'
    ),
    path('api/v1/paciente/expediente', # urls list all and create new expediente
        views.get_post_expedientes.as_view(),
        name='get_post_expedientes'
    ),
    re_path(r'^api/v1/paciente/sucursal/(?P<pk>[0-9]+)$', # Url to get update or delete a expediente
        views.get_delete_update_sucursal.as_view(),
        name='get_delete_update_sucursal'
    ),
    path('api/v1/paciente/sucursal', # urls list all and create new expediente
        views.get_post_sucursals.as_view(),
        name='get_post_sucursals'
    ),
    re_path(r'^api/v1/paciente/disponibilidadServ/(?P<pk>[0-9]+)$', # Url to get update or delete a disponibilidadservicio
        views.get_delete_update_disponibilidadServicio.as_view(),
        name='get_delete_update_disponibilidadServicio'
    ),
    path('api/v1/paciente/disponibilidadServ', # urls list all and create new disponibilidadservicio
        views.get_post_disponibilidadServicios.as_view(),
        name='get_post_disponibilidadServicios'
    ),
    re_path(r'^api/v1/paciente/estudio/(?P<pk>[0-9]+)$', # Url to get update or delete a estudio
        views.get_delete_update_estudio.as_view(),
        name='get_delete_update_estudio'
    ),
    path('api/v1/paciente/estudio', # urls list all and create new estudio
        views.get_post_estudios.as_view(),
        name='get_post_estudios'
    ),
    re_path(r'^api/v1/paciente/horarioSucursal/(?P<pk>[0-9]+)$', # Url to get update or delete a estudio
        views.get_delete_update_horarioSucursal.as_view(),
        name='get_delete_update_horarioSucursal'
    ),
    path('api/v1/paciente/horarioSucursal', # urls list all and create new estudio
        views.get_post_horarioSucursals.as_view(),
        name='get_post_horarioSucursals'
    ),
]
