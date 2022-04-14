import tabulate
from libAlumnos import (
    buscarAlumno,menu,
    insertarAlumno,actualizarAlumno,
    eliminarAlumno,cargarAlumnos,
    grabarAlumnos
)

#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D

####################################
menu()
opcion = 0
#alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]
#alumnos = []
#cargamos datos del archivo de texto
f = open('alumnos.txt','r')
strAlumnos = f.read()
alumnos = cargarAlumnos(strAlumnos)
f.close

while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        insertarAlumno(alumnos)
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
            actualizarAlumno(indexAlumno,alumnos)
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
           eliminarAlumno(indexAlumno,alumnos)
    elif(opcion == 5):
        #grabar lois datos en mi archivo de texto
        strAlumnos = grabarAlumnos(alumnos)
        #print(strAlumnos)
        fw = open('alumnos.txt','w')
        fw.write(strAlumnos)
        fw.close()
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")