import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import flash
from flask import session
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import *

from ..models import *
from ..views import *
from ..util import *
from registro import RegistroForm

#formulario para login
class LoginForm(Form):
    email = StringField('email', validators=[NumberRange(min=4)])
    password = PasswordField('password')
#login get
@app.route('/login/')
@logout_required
def regLog():
    formulario = LoginForm()
    regform = RegistroForm()
    data = get_user_cookie()
    return render_template("_views/registro_login.html", saves=data, loginForm = formulario, registroForm =regform)
#login post y validacion del login
@app.route('/login/', methods=['POST'])
@logout_required
def login():
    formulario = LoginForm(request.form)
    e_mail = formulario.data['email']
    clave = get_user_contrasena(e_mail)
    data = get_user_cookie()
    if formulario.validate() and clave == formulario.data['password']:
        session['email'] = e_mail
        session['username'] = formulario.data['email']
        data.update(formulario.data)
        response = make_response(redirect(url_for('index')))
        response.set_cookie('character', json.dumps(data))
    else :
        flash('Datos Incorrectos', 'danger')
        response = make_response(redirect(url_for('login')))
    return response
#logout del usuario
@app.route('/logout/')
@login_required
def loggout():

    response = make_response(redirect(url_for('index')))
    data = {}
    if 'username' in session:
        session.pop('username')
    if 'email' in session:
        session.pop('email')
    response.set_cookie('character', json.dumps(data))
    return response
