import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response

from login import *
from views import mysql
def insert_usuario(data):
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO usuario (nombre, apellidos, fecha_nacimiento, direccion, email, telefono, contrasena)
	VALUES (%s, %s, %s, %s, %s, %s, %s)''', (data.get('userLogin[nombre]', ' '), data.get('userLogin[apellidos]', ' '), data.get('userLogin[nacimiento]', ' '), data.get('userLogin[direccion]', ' '), data.get('userLogin[email]', ' '), data.get('userLogin[telefono]', ' '), data.get('userLogin[password]', ' ')))
	mysql.connection.commit()


@app.route('/registro', methods=['POST'])
def registro():
	response = make_response( redirect(url_for('perfil')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	insert_usuario(data)
	response.set_cookie('character', json.dumps(data))
	return response
