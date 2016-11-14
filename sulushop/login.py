import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response



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
		
@app.route('/login/', methods=['POST'])#todo meter datos en base
def login():
	response = make_response(redirect(url_for('index')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response


