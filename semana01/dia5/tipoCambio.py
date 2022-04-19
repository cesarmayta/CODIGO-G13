class tipoCambio:
    
    def __init__(self,tipoMonedas,montoCambio):
        self.tipoMonedas = tipoMonedas
        self.montoCambio = montoCambio
        
    def convertirSolesA(self,monto):
        return monto / self.montoCambio
    
    def convertirASoles(self,monto):
        return monto * self.montoCambio
    
SolesADolares = tipoCambio('Soles a Dolares',3.73)
DolaresASoles = tipoCambio('dolares a soles',3.88)

print("1 ) soles a dolares")
print("2 ) dolares a soles")
opcion = input("ingrese opcion")
monto = float(input("ingrese monto"))
if(opcion == "1"):
    resultado = "el resultado es  " +  str(SolesADolares.convertirSolesA(monto))
elif(opcion == "2"):
    resultado = "el restultado es " + str(DolaresASoles.convertirASoles(monto))
else:
    resultado = "No tenemos ese cambio"
    
print(resultado)