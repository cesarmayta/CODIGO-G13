from django.urls import path

from . import views

app_name = 'appfront'

urlpatterns = [
    path('',views.app_index,name='index'),
    path('<int:pregunta_id>',views.detalle,name='detalle'),
    path('enviar',views.enviar,name='enviar')
]