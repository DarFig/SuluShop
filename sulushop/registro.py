import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response

from login import *

#def insert_usuario(data):
#	cur = mysql.connection.cursor()
#	cur.execute('''INSERT INTO usuario (nombre, apellidos, fecha_nacimiento, direccion, #email, telefono, contrasena) VALLUES (?, ?, ?, ?, ?, ?, ?)''' % (
#		data.get('nombre', ' '), data.get('apellidos', ' '), data.get('nacimiento', #' '), data.get('direccion', ' '), data.get('email', ' '), data.get('telefono', ' '), data.get('clave', ' ')
	
#	))
	
	

@app.route('/registro', methods=['POST'])#todo meter datos en base
def registro():
	response = make_response( redirect(url_for('perfil')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response
