from flask import render_template

from . import admin

#importamos los formularios
from app.forms import LoginForm

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/login')
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    return render_template('admin/login.html',**context)