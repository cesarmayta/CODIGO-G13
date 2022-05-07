class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self,producto,qty):
        self.cart[producto.id] = {
            "producto_id" : producto.id,
            "nombre": producto.nombre,
            "cantidad": qty,
            "precio": str(producto.precio),
            "imagen" : producto.imagen.url,
            "total" : str(qty * producto.precio)
        }
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        