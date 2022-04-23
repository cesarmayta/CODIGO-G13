from flask import (
    render_template,redirect,
    url_for,session,
    flash)

from . import admin

#importamos los formularios
from app.forms import LoginForm, ProyectoForm


#### para autenticación de usuarios #######
import pyrebase
from app.auth_token import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
###########################################

from app.firebaseAdmin import db

@admin.route('/')
def index():
    if('token' in session):
        return render_template('admin/index.html')
    else:
        return redirect(url_for('admin.login'))
        
@admin.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    #CODIGO PARA LOGIN DE USUARIOS
    if login_form.validate_on_submit():
        usuarioData = login_form.usuario.data
        passwordData = login_form.password.data

        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            dataUsuarioValido = auth.get_account_info(usuario['idToken'])
            print(dataUsuarioValido)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
        except:
            print("usuario incorrecto")
            flash("Usuario o password invalidos")

    return render_template('admin/login.html',**context)

@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.login'))

@admin.route('/proyectos',methods=['GET','POST'])
def proyectos():
    if('token' in session):
        #formulario de proyectos
        colProyectos = db.collection('proyectos')
        proyecto_form = ProyectoForm()

        if proyecto_form.validate_on_submit():
            codigo = proyecto_form.codigo.data
            nombre = proyecto_form.nombre.data
            descripcion = proyecto_form.descripcion.data
            imagen = proyecto_form.imagen.data
            url = proyecto_form.url.data

            dataNuevoProyecto = {
                'codigo':codigo,
                'nombre':nombre,
                'descripcion':descripcion,
                'imagen':imagen,
                'url':url
            }
        
            colProyectos.document().set(dataNuevoProyecto)

        #obtenemos los proyectos de firestore
       
        docProyectos = colProyectos.get()
        lstProyectos= []
        for doc in docProyectos:
            dicProyecto = doc.to_dict()
            lstProyectos.append(dicProyecto)

        context = {
            'proyectos':lstProyectos,
            'proyecto_form':proyecto_form
        }
        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))
