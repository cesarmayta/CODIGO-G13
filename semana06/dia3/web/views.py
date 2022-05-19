from django.shortcuts import render,redirect

from .models import Categoria, PedidoDetalle,Producto



# Create your views here.
def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)

def productosPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias
    }
    return render(request,'index.html',context)

########### CARRITO DE COMPRAS ##############

from web.carrito import Cart

def carrito(request):
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    """
    funcion que elimina un producto del carrito de compras
    """
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()
    return render(request,'carrito.html')

############# LOGIN DE USUARIOS ###################

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def loginUsuario(request):
    context = {}
    if request.method ==  'POST':
        #login de usuarios
        dataUsuario = request.POST['usuario']
        dataPassword = request.POST['password']

        usuarioAuth = authenticate(request,username=dataUsuario,password=dataPassword)
        if usuarioAuth is not None:
            login(request,usuarioAuth)
            return redirect('/cuenta')
        else:
            context = {
                'error':'datos incorrectos'
            }

    return render(request,'login.html',context)

def crearUsuario(request):
    if request.method == 'POST':
        #registramos un nuevo usuario
        dataUsuario = request.POST['nuevoUsuario']
        dataPassword = request.POST['nuevoPassword']

        nuevoUsuario = User.objects.create_user(username=dataUsuario,password=dataPassword)
        login(request,nuevoUsuario)

        return redirect('/cuenta')

from .forms import ClienteForm
from .models import Cliente

def cuentaUsuario(request):
    #buscar si existe el cliente del usuario
    try:
        clienteEditar = Cliente.objects.get(usuario = request.user)
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email': request.user.email,
            'direccion':clienteEditar.direccion,
            'telefono':clienteEditar.telefono,
            'usuario':request.user.username
        }
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email': request.user.email,
            'usuario':request.user.username
        }


    frmCliente = ClienteForm(dataCliente)
    context = {
        'frmCliente': frmCliente
    }

    return render(request,'cuenta.html',context)

def actualizarCliente(request):
    mensaje = ""
    if request.method == 'POST':
        frmCliente = ClienteForm(request.POST)
        if frmCliente.is_valid():
            dataCliente = frmCliente.cleaned_data

            #actualización de usuario
            actUsuario = User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()

            try:
                actCliente = Cliente.objects.get(usuario = request.user)
                actCliente.direccion = dataCliente["direccion"]
                actCliente.telefono = dataCliente["telefono"]
                actCliente.save()
            except:
                nuevoCliente = Cliente()
                nuevoCliente.usuario = actUsuario
                nuevoCliente.direccion = dataCliente["direccion"]
                nuevoCliente.telefono = dataCliente["telefono"]
                nuevoCliente.save()
            
            mensaje = "DATOS ACTUALIZADOS CORRECTAMENTE"
        else:
            mensaje = "ERROR AL ACTUALIZAR LOS DATOS"

    context = {
        'mensaje':mensaje,
        'frmCliente':frmCliente
    }

    return render(request,'cuenta.html',context)


########### PEDIDOS ########################
from .models import Pedido,PedidoDetalle

#### PARA PAYPAL
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

def registrarPedido(request):
    if request.user.id is not None:
        #registra cabecera del pedido
        try:
            clientePedido = Cliente.objects.get(usuario=request.user)
            nuevoPedido = Pedido()
            nuevoPedido.cliente = clientePedido
            nuevoPedido.save()

            #registra detalle del pedido
            carritoPedido = request.session.get("cart")
            totalPedido = 0
            for key,value in carritoPedido.items():

                productoPedido = Producto.objects.get(pk=value["producto_id"])

                nuevoPedidoDetalle = PedidoDetalle()
                nuevoPedidoDetalle.pedido = nuevoPedido
                nuevoPedidoDetalle.producto = productoPedido
                nuevoPedidoDetalle.cantidad = int(value["cantidad"])
                nuevoPedidoDetalle.save()
                totalPedido += float(value["cantidad"]) * float(productoPedido.precio)

            #### REGISTRAMOS EL TOTAL DEL PEDIDO
            nuevoPedido.total = totalPedido
            nuevoPedido.save()

            ###BOTON DE PAYPAL
            request.session['paypal_pid'] = nuevoPedido.id
            host = request.get_host()
            paypal_datos = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': totalPedido,
                'item_name':'PEDIDO #' + str(nuevoPedido.id),
                'invoice': str(nuevoPedido.id),
                'notify_url':'http://' + host + '/' + 'paypal-ipn',
                'return_url':'http://' + host + '/' + 'pedidopagado'
            }

            formPedidoPaypal = PayPalPaymentsForm(initial=paypal_datos)

            context = {
                'pedido':nuevoPedido,
                'formpaypal':formPedidoPaypal
            }


            carrito = Cart(request)
            carrito.clear()

            return render(request,'pago.html',context)
        except:
            return redirect('/login')
    else:
        return redirect('/login')

def pedidopagado(request):
    pedidoID = request.session.get("paypal_pid")
    nroRecibo = request.GET.get('PayerID','')
    print("nro de recibo paypal:" + nroRecibo)
    print("id de pedido : " + str(pedidoID))
    pedidoEditar = Pedido.objects.get(pk=pedidoID)
    pedidoEditar.estado = 'pagado'
    pedidoEditar.nro_recibo = nroRecibo
    pedidoEditar.save()

    return render(request,'gracias.html')



