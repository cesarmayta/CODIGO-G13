#tabla de multiplicar
n = int(input("ingresa la tabla de multiplicar que desea mostrar : "))
c = 1
while(c <= 12):
    valor = n * c
    print(str(n) + " X " + str(c) + " = " + str(valor))
    c += 1
