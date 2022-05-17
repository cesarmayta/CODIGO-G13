from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
class Mesa(models.Model):
    mesa_id = models.AutoField(primary_key=True)
    mesa_nro = models.CharField(max_length=10,verbose_name="Nro Mesa")
    mesa_cap = models.IntegerField(default=0,verbose_name="Capacidad")

    def __str__(self):
        return self.mesa_nro

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nom = models.CharField(max_length=100,verbose_name='nombre')

    def __str__(self):
        return self.categoria_nom

class Plato(models.Model):
    plato_id = models.AutoField(primary_key=True)
    plato_nom = models.CharField(max_length=200,verbose_name='nombre')
    plato_img = CloudinaryField('image',default='')
    plato_pre = models.DecimalField(max_digits=10,decimal_places=2,default=0,
                                    verbose_name='precio')
    categoria_id = models.ForeignKey(Categoria,related_name='Platos',
                                    to_field='categoria_id',on_delete=models.RESTRICT,
                                    db_column='categoria_id',verbose_name='categoria')

    def __str__(self):
        return self.plato_nom

from django.contrib.auth.models import User

class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    pedido_fech = models.DateTimeField(null=True,verbose_name='Fecha')
    pedido_nro = models.CharField(max_length=100,default='',verbose_name='Nro Pedido')
    pedido_est = models.CharField(max_length=100,default='pagado',verbose_name='Estado')
    usu_id = models.ForeignKey(User,to_field='id',related_name='Pedidos',
                                on_delete=models.RESTRICT,
                                db_column='usu_id',verbose_name='Usuario')
    mesa_id = models.ForeignKey(Mesa,to_field='mesa_id',on_delete=models.RESTRICT,
                                db_column='mesa_id',verbose_name='Mesa')

class PedidoPlato(models.Model):
    pedidoplato_id = models.AutoField(primary_key=True)
    pedidoplato_cant = models.IntegerField(default=1)
    plato_id = models.ForeignKey(Plato,related_name='pedidoplatos',to_field='plato_id',
                                on_delete=models.RESTRICT,db_column='plato_id',
                                verbose_name='Plato')
    pedido_id = models.ForeignKey(Pedido,related_name='pedidoplatos',to_field='pedido_id',
                                  on_delete=models.RESTRICT,db_column='pedido_id',
                                  verbose_name='Pedido')




