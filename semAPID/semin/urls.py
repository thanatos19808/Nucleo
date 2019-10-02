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

]
