#similar a json
capitales = {
    'Perú':'lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Uruguay':'Montevideo'    
}
print(capitales)
nuevaCapital = {'Brasil':'Brasilia'}
#agregar nuevo valor al diccionario
capitales.update(nuevaCapital)
print(capitales)
#eliminar valores del diccionario
c = capitales.pop('Chile','no existe ese pais en mi diccionario')
print(c)
print(capitales)
### RECORRER DICCIONARIOS
for capital in capitales:
    print(capital + " : " + capitales[capital])
print(capitales.keys())
print(capitales.values())
print(capitales.items())
for clave in capitales.keys():
    print(clave + " => " + capitales[clave])
    
for clave,valor in capitales.items():
    print(clave + " -- " + valor)
#### BASE DE DATOS DE ALUMNOS ###
alumno1 = {
    'Nombre':'César Mayta',
    'Edad':39,
    'Nota':19.5,
    'aprobado':True,
    'cursos':['Javacript','Python','C#']
}
alumno2 = {
    'Nombre':'Lucia Torres',
    'Edad':29,
    'Nota':20,
    'aprobado':True,
    'cursos':['Java','Swift','Kotlin']
}
alumnos = [alumno1,alumno2]
print("*" * 100)
for columna in alumno1:
    print(columna,end = '       | ')
print()
print("*" * 100)
for alumno in alumnos:
    for clave,valor in alumno.items():
        print(valor,end = '     |    ')
    print()



