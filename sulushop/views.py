from sulushop import app
from flask import jsonify
from flask import request
from flask import render_template


from models import *
from util import *
from decorators import *


from controllers.registro import *
from controllers.carrito import *
from controllers.login import *
from controllers.perfil import *
from controllers.detalles import *


@app.route('/')
def index():
    lista = Producto.query.all()
    for producto in lista:
        insert_atributes(producto)
    return render_template('_views/lista.html', productos=lista)
    
def insertar_foto(producto):
    picture = get_product_cover(producto.id)
    url = Template('/detalles/$id') 
    producto.url = url.substitute(id=producto.id)
    if picture:
        producto.picture = picture
