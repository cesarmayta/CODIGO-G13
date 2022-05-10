from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto,Cliente,Pedido,PedidoDetalle

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
