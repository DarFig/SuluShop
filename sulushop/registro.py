import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response

from login import *
#from views import *
#def insert_usuario(data):
#	cur = mysql.connection.cursor()
#	cur.execute('''INSERT INTO usuario (nombre, apellidos, fecha_nacimiento, direccion, #email, telefono, contrasena) VALLUES (%s)''' % (
#		data.get('userLogin[nombre]', ' '), data.get('userLogin[apellidos]', ' '), data.get('userLogin[nacimiento]', ' '), data.get('userLogin[direccion]', ' '), data.get('userLogin[email]', ' '), data.get('userLogin[telefono]', ' '), data.get('userLogin[password]', ' ')
#
#	))



@app.route('/registro', methods=['POST'])#todo meter datos en base
def registro():
	response = make_response( redirect(url_for('perfil')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response
