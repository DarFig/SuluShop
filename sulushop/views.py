from sulushop import app
from flask import render_template

from models import *
from util import *
from decorators import *

from controllers.registro import *
from controllers.carrito import *
from controllers.login import *
from controllers.perfil import *
from controllers.detalle import *


@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    lista = Producto.query.paginate(page, 20, False)
    form = AddToCart()
    for producto in lista.items:
        insert_atributes(producto)

    return render_template('_views/lista.html',
            productos=lista,
            form=form,)


def insert_atributes(producto):
    picture = get_product_cover(producto.id)
    if picture:
        producto.picture = picture
