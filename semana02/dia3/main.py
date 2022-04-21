from pydoc import doc
from flask import Flask,render_template,request
#import requests

#URL = 'https://api.github.com/users/cesarmayta'


## para conectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

### para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()

colBiografia = db.collection('biografia')
docBiografia = colBiografia.get()

for doc in docBiografia:
    dicBiografia = doc.to_dict()


app = Flask(__name__)

@app.route('/')
def index():
    #return '<center><H1>BIENVENIDO A MI SITIO WEB</H1></center>'
    
    context = {
        'biografia':dicBiografia
    }
    #data = requests.get(URL)

    #nombre = request.args.get('nombre','')
    #context = data.json()
    #print(context)

    return render_template('home.html',**context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA','ENCANTO','SONIC 2']

    nombre = request.args.get('nombre','')

    context = {
        'nombre':nombre,
        'peliculas':listaPeliculas
    }
    return render_template('peliculas.html',**context)

############### RUTAS DE MIS PAGINAS
@app.route('/acercade')
def about():
    context = {
        'biografia':dicBiografia
    }
    return render_template('acercade.html',**context)

@app.route('/portafolio')
def portafolio():
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
    return render_template('portafolio.html',**context)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)