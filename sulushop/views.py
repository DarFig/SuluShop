from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template


from models import *
from util import *
from decorators import *


# from controllers.registro import *
from controllers.carrito import *
# from controllers.login import *
# from controllers.perfil import *


@app.route('/')
def index():
    return render_template('_views/lista.html')
