from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    #return '<center><H1>BIENVENIDO A MI SITIO WEB</H1></center>'
    
    nombre = request.args.get('nombre','')

    context = {
        'nombre':nombre
    }

    return render_template('index.html',**context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA','ENCANTO','SONIC 2']

    nombre = request.args.get('nombre','')

    context = {
        'nombre':nombre,
        'peliculas':listaPeliculas
    }
    return render_template('peliculas.html',**context)

app.run(debug=True)