import json
from sulushop import app
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import make_response
from flask import flash

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import *


from ..models import *
from ..views import *
from ..util import *

class cambioForm(Form):
	oldPassword = PasswordField('oldpassword')
	newPassword = PasswordField('newpassword')
	repeatPassword = PasswordField('repeatpassword')
'''
Router: 	solo accesible mediante el método POST de HTTP/HTTPS

Descripcion: 	cambio() toma los datos del formulario cambioForm y los analiza. oldPassword es la contrasena del usuario
		antigua que quiere cambiar, si no coincide con la almacenada en la base de datos, aparece un mensaje de
		error. newPassword y repeatPassword son la nueva contrasena deseada, si no coinciden, aparece un mensaje
		de error. Si todo es correcto,la antigua contrasena sustituye a la nueva contrasena en la base de datos
Funcion:	Cambia la contrasena del usuario
'''
@app.route('/change', methods=['POST'])
@logout_required
def cambio():
	formulario = cambioForm(request.form)
	if formulario.newPassword != formulario.repeatPassword:
		flash('Las contrasenas no coinciden', 'danger')
        return make_response(redirect(url_for('password')))
	contrasenaa = Usuario.query.filter_by(id=get_user_id()).first().contrasena
	if formulario.oldPassword != contrasena:
		flash('Contrasena incorrecta', 'danger')
        return make_response(redirect(url_for('password')))
	user = Usuario.query.filter_by(id=get_user_id()).first()
	user.contrasena = contrasenaa
	db.session.commit()
	response = make_response( redirect(url_for('perfil')))
	return response
