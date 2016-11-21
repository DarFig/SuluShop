from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template

<<<<<<< HEAD
from controllers.registro import *
=======

from models import *
from util import *
from decorators import *


# from controllers.registro import *
>>>>>>> e2c52ea00cf4ea81cf1fc797cd4ed0c659f3a1d8
from controllers.carrito import *
from controllers.login import *
from controllers.perfil import *


@app.route('/')
def index():
    return render_template('_views/lista.html')
