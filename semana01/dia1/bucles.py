opcion = 0
while(opcion == 0):
    print(" ============== OPCIONES ==========")
    print(" 1) opción 01")
    print(" 2) opción 02")
    print(" 3) opción 03")
    opcion = int(input("opción elegida :"))
    print("ud selecciono la opción " + str(opcion))
    salir = input("desea salir (si/no)")
    if(salir == "no"):
        opcion = 0
    
    