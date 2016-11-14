from sulushop import app
from flask import request
from flask import render_template

from login import *

@app.route('/perfil/')
def perfil():
	data = get_user_cookie()
	return render_template("_views/perfil.html", saves=data)
