import json
from sulushop import app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response


from login import *

@app.route('/registro', methods=['POST'])#todo
def registro():
	response = make_response( redirect(url_for('perfil')))
	data = get_user_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response
