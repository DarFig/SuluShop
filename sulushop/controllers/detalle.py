#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sulushop import app
from flask import render_template


from ..models import *
from ..util import *
from ..decorators import *
from carrito import AddToCart
from favorito import UpdateList


@app.route('/<name>/<int:pk>/', methods=['GET'])
def details(name, pk):
    product = Producto.query.get(pk)
    cover = get_product_cover(pk)
    score = calc_score(pk)
    form = AddToCart()
    favorites = UpdateList()

    return render_template('_views/detalle.html',
            product=product,
            cover=cover,
            score=score,
            form=form,
            favorites=favorites)


def calc_score(pk):
    scores = Puntuacion.query.filter_by(id_producto=pk).all()
    score = 0

    for num in scores:
        score += num['puntuacion']

    if score != 0 and len(scores) != 0:
        score = score/len(scores)
    return score
