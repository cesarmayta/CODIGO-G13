from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('producto',views.ProductoView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaProductoView.as_view()),
    path('usuario/<int:usuario_id>',views.UsuarioView.as_view())
]