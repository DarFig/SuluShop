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

class CambioForm(Form):
	oldPassword = PasswordField('oldpassword')
	newPassword = PasswordField('newpassword')
	repeatPassword = PasswordField('repeatpassword')


@app.route('/changePassword/', methods=['GET'])
@login_required
def cambiarpassw():
	formulario = CambioForm()
	data = get_user_cookie()
	return render_template("_modules/password.html", saves=data, cambioForm = formulario)

@app.route('/changePassword/', methods=['POST'])
@login_required
def cambiopassw():
	formulario = CambioForm(request.form)
	usuario = get_user()
	if formulario.data['newPassword'] == formulario.data['repeatPassword'] :
		if formulario.data['oldPassword'] == usuario.contrasena:
			db.session.delete(usuario)
			usuario.contrasena = formulario.data['newPassword']
			db.session.add(usuario)
			db.session.commit()
			return make_response(redirect(url_for('perfil')))
		else :
			flash('Contrasena incorrecta', 'danger')
	        return make_response(redirect(url_for('cambiopassw')))
	else :
		flash('Las contrasenas no coinciden', 'danger')
        return make_response(redirect(url_for('cambiopassw')))
