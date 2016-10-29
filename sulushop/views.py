import json
from sulushop import app
from flask import request
from flask import (render_template, redirect, url_for
								, request, make_response)


@app.route('/')
def index():
    return render_template("_modules/lista.html");
	

@app.route('/')
@app.route('/registro_login.html')
def regLog():
	return render_template("_modules/registro_login.html");
	
	
@app.route('/')
@app.route('/templates/_modules/perfil.html')
def perfil():
	return render_template("_modules/perfil.html");

@app.route('/login', methods=['POST'])#todo
def login():
	response = make_response( redirect(url_for('index')))
	return response;	
	
@app.route('/registro', methods=['POST'])#todo
def registro():
	response = make_response( redirect(url_for('perfil')))
	return response;	