class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart") #canasta del carrito
        montoTotal = self.session.get("cartMontoTotal")
        if not cart:
            cart = self.session["cart"] = {}
            montoTotal = self.session["cartMontoTotal"] = "0"
        self.cart = cart
        self.montoTotal = float(montoTotal)
    
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

    def delete(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def clear(self):
        self.session["cart"] = {}
        self.session["cartMontoTotal"] = "0"
        
    def save(self):
        montoTotal = 0
        for key,value in self.cart.items():
            montoTotal += float(value["total"])
        self.session["cartMontoTotal"] = montoTotal
        self.session["cart"] = self.cart
        self.session.modified = True

        