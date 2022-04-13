#entrada
tabla = int(input("Ingresa la tabla de multiplicar que desea mostrar : "))
#proceso
valor1 = tabla * 1;
valor2 = tabla * 2;
valor3 = tabla * 3;
#salida
print(str(tabla) + ' X 1 = ' + str(valor1))
print(str(tabla) + ' X 2 = ' + str(valor2))
print(str(tabla) + ' X 3 = ' + str(valor3))

#TABLA DE MULTIPLICAR USANDO FOR
print("TABLA USANDO FOR")
for contador in range(1,12,3):
    valor = tabla * contador
    #print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))
    print(tabla,' X ',contador,' = ',valor)
