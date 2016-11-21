from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template

from controllers.registro import *
from controllers.carrito import *
from controllers.login import *
from controllers.perfil import *

@app.route('/')
def index():
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM producto''')
    # summary = cur.fetchall()
    # data = map(list, summary)
    # return render_template('_views/lista.html', productos=data, logueado=log)
    log = get_user_cookie()
    return render_template('_views/lista.html')
