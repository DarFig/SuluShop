from sulushop import app
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from sqlalchemy.sql import func


from ..models import *
from ..util import *


def insert_atributes(producto):
    producto[0].total = producto[0].precio * producto[1]
    picture = get_product_cover(producto[0].id)
    if picture:
        producto[0].picture = picture


@app.route('/carrito/', methods = ['GET',])
@login_required
def cart():
    cart = Producto.query.join(Carro).filter(
            Carro.id_producto == Producto.id,
            Carro.id_usuario == get_user_id()
            ).add_columns(
                    Carro.cantidad,
                    ).all()

    total_price = 0

    for producto in cart:
        insert_atributes(producto)
        total_price += producto[0].total

    return render_template('_views/carrito.html', productos=cart, total=total_price)


@app.route('/carrito/', methods = ['POST',])
@login_required
def delete_all_cart():
    products = Carro.query.filter_by(id_usuario = get_user_id()).all()

    for cart in products:
        db.session.delete(cart)

    db.session.commit()

    # TODO: redirect to index
    return make_response(redirect(url_for('cart')))


@app.route('/carrito/add/', methods = ['POST',])
@login_required
def add_cart():
    pk = request.form['pk']
    quantity = request.form['cantidad']

    product = Carro(quantity, get_user_id(), pk)
    db.session.add(product)
    db.session.commit()

    return make_response(redirect(url_for('cart')))


@app.route('/carrito/delete/', methods = ['POST',])
@login_required
def delete_cart():
    pk = request.form['pk']

    products = Carro.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            ).all()

    for cart in products:
        db.session.delete(cart)

    db.session.commit()

    return make_response(redirect(url_for('cart')))
