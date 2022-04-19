class moneda:
    
    def __init__(self,tipo,camSoles):
        self.tipo = tipo
        self.cambioSoles = camSoles
        
    def mostrar(self):
        print("la moneda es " + self.tipo + " y su tipo de cambio a soles es " + str(self.cambioSoles))
        
    def convertir(self,monto,origen):
        if(origen == "soles"):
            resultado = monto * self.cambioSoles
        else:
            resultado =  monto / self.cambioSoles
        return resultado
        

monedaDolares = moneda('dolares',3.71)
monedaEuros = moneda('euros',4.10)

monedaDolares.mostrar()
monedaEuros.mostrar()
#ENTRADAS
origen = input("ingrese moneda origen:")
destino = input("Ingrese moneda destino:")
montoOrigen = float(input("ingrese el monto : "))

#PROCESO
if(origen == "soles" and destino ==  "dolares"):
    resultado = monedaDolares.convertir(montoOrigen,destino)
elif(origen == "soles" and destino ==  "euros"):
    resultado = monedaEuros.convertir(montoOrigen,destino)
elif(origen == "dolares" and destino == "soles"):
    resultado = monedaDolares.convertir(montoOrigen,destino)
elif(origen == "euros" and destino == "soles"):
    resultado = monedaEuros.convertir(montoOrigen.destino)
    
#SALIDAS
print(" ===================================== ")
print(" monto origen : " + str(montoOrigen) + " " + str(origen))
print(" moneda destino : " + str(destino))
print(" resultado : " + str(resultado) + " " + str(destino))
