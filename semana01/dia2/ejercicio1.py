#CREAR UN CUADRADO CON *
#ENTRADA
lado =  int(input("ingrese la lado del cuadrado : "))
#PROCESO
"""
ingreso 5
* * * * *
*       *
*       *
*       *
* * * * *
"""
total = lado + 1
for contador in range(1,total):
    if(contador == 1 or contador == lado):
        print('* ' * lado)
    else:
        for columna in range(1,total):
            if(columna == 1 or columna == lado):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        #print('* ' + '  ' * (lado - 2) + '*')