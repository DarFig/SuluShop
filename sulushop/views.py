from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import url_for
from flask_mysqldb import MySQL

mysql = MySQL(app)

from carrito import *


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tienda_producto''')
    summary = cur.fetchall()
    data = map(list, summary)
    return render_template('_views/lista.html', productos=data)
    # productos = jsonify(productos=cur.fetchall())
    # return render_template("_views/lista.html", productos=productos)


@app.route('/login/')
def regLog():
    return render_template("_views/registro_login.html")


@app.route('/perfil/')
def perfil():
    return render_template("_views/perfil.html")

@app.route('/login', methods=['POST'])#todo
def login():
    response = make_response( redirect(url_for('index')))
    return response

@app.route('/registro', methods=['POST'])#todo
def registro():
    response = make_response( redirect(url_for('perfil')))
    return response
