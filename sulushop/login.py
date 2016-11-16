import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import session

from views import mysql

def get_user_cookie():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data

@app.route('/login/')
def regLog():
	data = get_user_cookie()
	return render_template("_views/registro_login.html", saves=data)

@app.route('/login/', methods=['POST'])
def login():
	formulario = dict(request.form.items())
	data = get_user_cookie()
	cur = mysql.connection.cursor()
	cur.execute('''SELECT contrasena FROM usuario where email = %s ''', [formulario.get('userLogin[email]', ' ')] )
	clave = cur.fetchone()
	
	if clave and formulario.get('userLogin[password]', ' ') == clave[0]:
		data.update(dict(request.form.items()))
		response = make_response(redirect(url_for('index')))
		response.set_cookie('character', json.dumps(data))
	else :
		response = make_response(redirect(url_for('login')))
	return response

@app.route('/logout/')
def loggout():
	response = make_response(redirect(url_for('index')))
	data = {}
	response.set_cookie('character', json.dumps(data))
	return response
