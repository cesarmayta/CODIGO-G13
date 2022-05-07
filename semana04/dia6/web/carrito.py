class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart") #canasta del carrito
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self,producto,qty):
        if (str(producto.id) not in self.cart.keys()):
            self.cart[producto.id] = {
                "producto_id" : producto.id,
                "nombre": producto.nombre,
                "cantidad": qty,
                "precio": str(producto.precio),
                "imagen" : producto.imagen.url,
                "total" : str(qty * producto.precio),
                "categoria": producto.categoria.nombre
            }
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + qty)
                    value["total"] = str(float(value['cantidad']) * float(value['precio']))
                    break
            
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

        