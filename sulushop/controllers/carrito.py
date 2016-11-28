#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from sulushop import app
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange, DataRequired


from ..models import *
from ..util import *
from ..decorators import *


class UpdateCart(FlaskForm):
    pk = IntegerField('pk', validators=[NumberRange(min=0)])
    name = StringField('name', validators=[DataRequired()])


class AddToCart(UpdateCart):
    quantity = IntegerField('quantity', validators=[NumberRange(min=1)])


def insert_atributes(producto):
    producto[0].total = producto[0].precio * producto[1]
    picture = get_product_cover(producto[0].id)
    if picture:
        producto[0].picture = picture


@app.route('/carrito/', methods=['GET'])
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

    form = UpdateCart()

    return render_template('_views/carrito.html', productos=cart, total=total_price, form=form)


@app.route('/carrito/', methods=['POST'])
@login_required
def delete_all_cart():
    products = Carro.query.filter_by(id_usuario = get_user_id()).all()

    for cart in products:
        lista = Lista();
        lista.id_usuario = get_user_id()
        lista.id_producto = cart.id_producto
        lista.fecha = datetime.datetime.utcnow()
        lista.cantidad = cart.cantidad
        producto = Producto.query.get(cart.id_producto)
        lista.precio = producto.precio
        lista.accion = 'Comprado'

        db.session.add(lista)
        db.session.delete(cart)
        flash('Has eliminado {} del carrito'.format(
            producto.nombre), 'danger')

    db.session.commit()

    return make_response(redirect(url_for('index')))


@app.route('/carrito/add/', methods=['POST'])
@login_required
def add_cart():
    form = AddToCart(request.form)
    quantity = form.data['quantity']
    pk = form.data['pk']
    name = form.data['name']

    if form.validate_on_submit():
        product = Carro()
        product.cantidad = quantity
        product.id_producto = pk
        product.id_usuario = get_user_id()
        db.session.add(product)

        db.session.commit()

        flash('Has añadido {} al carrito'.format(name), 'success')

    return make_response(redirect(url_for('cart')))


@app.route('/carrito/delete/', methods=['POST'])
@login_required
def delete_cart():
    form = UpdateCart(request.form)
    pk = form.data['pk']
    name = form.data['name']

    if form.validate_on_submit():
        products = Carro.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            ).all()

        for cart in products:
            db.session.delete(cart)
            flash('Has eliminado {} del carrito'.format(name), 'danger')

        db.session.commit()

    return make_response(redirect(url_for('cart')))
