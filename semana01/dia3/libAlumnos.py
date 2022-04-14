#LIBRERIA DE ALUMNOS
######### FUNCIONES ################
def menu():
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
    
def buscarAlumno(valorBusqueda,alumnos):
    indexAlumno = -1
    for i in range(len(alumnos)):
        dicAlumnoBusqueda = alumnos[i]
        for clave,valor in dicAlumnoBusqueda.items():
            if(valor == valorBusqueda and clave == 'email'):
                indexAlumno = i
                break
    return indexAlumno

def insertarAlumno(alumnos):
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
        
def actualizarAlumno(indexAlumno,alumnos):
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
    
def eliminarAlumno(indexAlumno,alumnos):
    alumnos.pop(indexAlumno)
    print("ALUMNO ELIMINADO !!!")