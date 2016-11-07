import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import url_for


from carrito import *


@app.route('/')
def index():
    return render_template("_modules/lista.html")


@app.route('/')
@app.route('/registro_login.html')
def regLog():
    return render_template("_views/registro_login.html")


@app.route('/')
@app.route('/templates/_modules/perfil.html')
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
