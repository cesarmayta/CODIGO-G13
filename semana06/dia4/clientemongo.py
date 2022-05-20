from pymongo import MongoClient 

cliente = MongoClient('mongodb://127.0.0.1:27017')

db = cliente['cursos']

colAlumnos = db['alumnos']

dicNuevoAlumno = {
    "nombre":"Pedro Fernandez",
    "email":"pedrito@gmail.com",
    "nota":7
}

nuevoAlumnoId = colAlumnos.insert_one(dicNuevoAlumno)

print("Nuevo Alumno" + str(nuevoAlumnoId))


for alumno in colAlumnos.find():
    print(alumno["nombre"] + " - " + alumno["email"] + " - " + str(alumno["nota"]))