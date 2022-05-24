from mongoengine import Document,EmbeddedDocument,fields

class Alumno(EmbeddedDocument):
    nombre = fields.StringField(required=True)
    email = fields.EmailField(required=True)


class Curso(EmbeddedDocument):
    nombre = fields.StringField(required=True)


class Matricula(Document):
    nro = fields.StringField(required=True)
    alumno = fields.EmbeddedDocumentField(Alumno)
    cursos = fields.ListField(fields.EmbeddedDocumentField(Curso))