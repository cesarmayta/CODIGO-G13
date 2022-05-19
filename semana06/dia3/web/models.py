from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.telefono

class Pedido(models.Model):
    SOLICITADO = 'solicitado'
    PAGADO = 'pagado'

    ESTADO_CHOICES = (
        (SOLICITADO,'Solicitado'),
        (PAGADO,'Pagado')
    )

    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20,default='solicitado',choices=ESTADO_CHOICES)
    nro_recibo = models.CharField(max_length=200,default='')
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    def __str__(self):
        return str(self.fecha_reg)

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return  self.producto.nombre
