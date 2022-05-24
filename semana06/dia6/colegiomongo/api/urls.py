from django.urls import path

from . import views

urlpatterns = [
    path('matricula', views.MatriculaView.as_view())
]
