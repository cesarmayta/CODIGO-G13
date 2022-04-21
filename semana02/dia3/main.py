from pydoc import doc
from flask import Flask,render_template,request
import requests

URL = 'https://api.github.com/users/cesarmayta'


app = Flask(__name__)

@app.route('/')
def index():
    #return '<center><H1>BIENVENIDO A MI SITIO WEB</H1></center>'
    data = requests.get(URL)

    #nombre = request.args.get('nombre','')
    context = data.json()
    print(context)

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
    return render_template('acercade.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)