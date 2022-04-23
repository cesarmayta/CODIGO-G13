from flask import Flask,render_template,request,session

from . import portafolio

## para conectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

### para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()


@portafolio.route('/')
def home():
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()

    session['biografia'] = dicBiografia

    #recuperamos la info de los enlaces
    colEnlaces = db.collection('enlaces')
    docEnlaces = colEnlaces.get()

    lstEnlaces = []
    for doc in docEnlaces:
        dicEnlace = doc.to_dict()
        lstEnlaces.append(dicEnlace)

    session['enlaces'] = lstEnlaces
    return render_template('portafolio/home.html')

############### RUTAS DE MIS PAGINAS
@portafolio.route('/acercade')
def about():
    return render_template('portafolio/acercade.html')

@portafolio.route('/proyectos')
def proyectos():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()

    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)


    context = {
        'proyectos':lstProyectos
    }
    return render_template('portafolio/portafolio.html',**context)

@portafolio.route('/contacto')
def contacto():
    return render_template('portafolio/contacto.html')

