from api.models import Matricula,Curso,Alumno

m = Matricula()
m.nro = '1234'
m.alumno = {
    'nombre':'tunombre',
    'email':'tuemail@gmail.com'
}
m.cursos = [
    {'nombre':'python'},{'nombre':'mongodb'},{'nombre':'mysql'}
]
m.save()