from flask import Flask,render_template,request,session
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

app = Flask(__name__)

#creamos una clave secreta para las variables de sesión
app.secret_key = 'qwerty123456'

@app.route('/')
def index():
    #return '<center><H1>BIENVENIDO A MI SITIO WEB</H1></center>'
    #recuperamos la info de la biografia
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


    #data = requests.get(URL)

    #nombre = request.args.get('nombre','')
    #context = data.json()
    #print(context)

    return render_template('home.html')

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
    return render_template('acercade.html')

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