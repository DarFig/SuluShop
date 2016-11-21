import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from sqlalchemy.sql import func

from ..models import *
from ..views import *
from ..util import *

def insert_usuario(data):
	usuario = Usuario()
	usuario.nombre = data.get('userLogin[nombre]', ' ')
	usuario.apellidos = data.get('userLogin[apellidos]', ' ')
	usuario.fecha_nacimiento = data.get('userLogin[nacimiento]', ' ')
	usuario.direccion = data.get('userLogin[direccion]', ' ')
	usuario.email = data.get('userLogin[email]', ' ')
	usuario.telefono = data.get('userLogin[telefono]', ' ')
	usuario.contrasena = data.get('userLogin[password]', ' ')
	usuario.imagen = '/static/img/avatar.jpg'
	db.session.add(usuario)
	db.session.commit()


@app.route('/registro', methods=['POST'])
@logout_required
def registro():
	response = make_response( redirect(url_for('perfil')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	insert_usuario(data)
	response.set_cookie('character', json.dumps(data))
	return response
