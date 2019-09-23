from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/paciente/(?P<pk>[0-9]+)$', # Url to get update or delete a  paciente
        views.get_delete_update_paciente.as_view(),
        name='get_delete_update_paciente'
    ),
    path('api/v1/pacientes/', # urls list all and create new one
        views.get_post_pacientes.as_view(),
        name='get_post_pacientes'
    )
]
