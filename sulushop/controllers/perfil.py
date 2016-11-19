from sulushop import app
from flask import request
from flask import render_template


from ..views import mysql
from ..util import *

@app.route('/deletUser/')
@login_required
def deletUser():
	data = get_user_cookie()
	cur = mysql.connection.cursor()
	cur.execute('''DELETE FROM usuario where email = %s
            ''', [data.get('userLogin[email]', ' ')] )
	mysql.connection.commit()
	response = make_response(redirect(url_for('index')))
	data = {}
	response.set_cookie('character', json.dumps(data))
	return response


@app.route('/perfil/')
@login_required
def perfil():
	data = get_user_cookie()
	cur = mysql.connection.cursor()
	cur.execute('''SELECT nombre, apellidos, fecha_nacimiento, direccion,
            telefono, email, imagen FROM usuario
            where email = %s ''', [data.get('userLogin[email]', ' ')] )
	summary = cur.fetchall()
	datos = map(list, summary)
	return render_template("_views/perfil.html", save=datos,logueado=data)
