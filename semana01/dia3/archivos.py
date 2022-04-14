"""
f = open('alumnos.txt','w')
f.write('cesar mayta,cesarmayta@gmail.com,242332\n')
f.write('ana lopez,ana@gmail.com,2232323\n')
f.write('jorge perez,jorge@gmail.com,242332')
"""

f = open('alumnos.txt','r')
alumnos = f.read()
print(alumnos)

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listaResultado = []

for dictAlumno in listaAlumnos:
    listaDiccionarioAlumnos = dictAlumno.split(',')
    print(listaDiccionarioAlumnos)
    dictAlumno = {
        'nombre':listaDiccionarioAlumnos[0],
        'email':listaDiccionarioAlumnos[1],
        'celular':listaDiccionarioAlumnos[2]
    }
    listaResultado.append(dictAlumno)

print(listaResultado)
f.close
    