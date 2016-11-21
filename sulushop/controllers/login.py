import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import session
from sqlalchemy.sql import func

from ..models import *
from ..views import *
from ..util import *


@app.route('/login/')
@logout_required
def regLog():
	data = get_user_cookie()
	return render_template("_views/registro_login.html", saves=data)

@app.route('/login/', methods=['POST'])
@logout_required
def login():
	formulario = dict(request.form.items())
	e_mail = formulario.get('userLogin[email]', ' ')
	clave = get_user_contrasena(e_mail)
	data = get_user_cookie()
	if clave and formulario.get('userLogin[password]', ' ') == clave:
		data.update(dict(request.form.items()))
		response = make_response(redirect(url_for('index')))
		response.set_cookie('character', json.dumps(data))
	else :
		response = make_response(redirect(url_for('login')))
	return response

@app.route('/logout/')
@login_required
def loggout():
	response = make_response(redirect(url_for('index')))
	data = {}
	response.set_cookie('character', json.dumps(data))
	return response
