from flask import render_template

from . import admin

#importamos los formularios
from app.forms import LoginForm


#### para autenticación de usuarios #######
import pyrebase
from app.auth_token import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
###########################################

@admin.route('/')
def index():
    return render_template('admin/index.html')

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
        except:
            print("usuario incorrecto")

    return render_template('admin/login.html',**context)