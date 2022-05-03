from django.urls import path

from . import views

urlpatterns = [
    path('',views.app_index,name='index'),
    path('<int:pregunta_id>',views.detalle,name='detalle')
]