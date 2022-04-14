import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
######### FUNCIONES ################
def buscarAlumno(valorBusqueda,alumnos):
    indexAlumno = -1
        for i in range(len(alumnos)):
            dicAlumnoBusqueda = alumnos[i]
            for clave,valor in dicAlumnoBusqueda.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break
    return indexAlumno
####################################
print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "* 8 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " "* 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " "* 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)
opcion = 0
alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A EDITAR
        valorBusqueda = input("Ingrese el email del alumno a actualizar : ")
        
        indexAlumno = buscarAlumno(valorBusqueda,alumnos)
        
        #PASO 2 INGRESAR LOS NUEVOS VALORES PARA EL ALUMNO A EDITAR
        if(indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
            nombre  = input("NOMBRE  : ")
            email   = input("EMAIL   : ")
            celular = input("CELULAR : ")
            dictAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            #PASO 3 ACTUALIZAR LOS DATOS DEL ALUMNO A EDITAR
            alumnos[indexAlumno] = dictAlumnoEditar
            print("ALUMNO ACTUALIZADO !!!")
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        #PASO 1 BUSCAR EL ALUMNO A ELIMINAR
        valorBusqueda = input("Ingrese el email del alumno a eliminar : ")
        
        indexAlumno = buscarAlumno(valorBusqueda,alumnos)
        
        #PASO 2 INGRESAR LOS NUEVOS VALORES PARA EL ALUMNO A ELIMINAR
        if(indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
            #ELIMINAR EL ALUMNO
            alumnos.pop(indexAlumno)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")