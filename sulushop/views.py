from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template
from flask_mysqldb import MySQL

mysql = MySQL(app)

from carrito import *
from login import *
from perfil import *
from registro import *

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tienda_producto''')
    summary = cur.fetchall()
    data = map(list, summary)
    return render_template('_views/lista.html', productos=data)
    # productos = jsonify(productos=cur.fetchall())
    # return render_template("_views/lista.html", productos=productos)



