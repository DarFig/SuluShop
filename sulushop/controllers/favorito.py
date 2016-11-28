#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from sulushop import app
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import NumberRange, DataRequired


from ..models import *
from ..util import *
from ..decorators import *


class UpdateList(FlaskForm):
    pk = IntegerField('pk', validators=[NumberRange(min=0)])
    name = StringField('name', validators=[DataRequired()])


@app.route('/lista/add/', methods=['POST'])
@login_required
def add_to_list():
    form = UpdateList(request.form)
    pk = form.data['pk']
    name = form.data['name']

    if form.validate_on_submit():
        product = Lista()
        product.accion = 'favorito'
        product.fecha = datetime.datetime.utcnow()
        product.id_usuario = get_user_id()
        product.id_producto = pk

        db.session.add(product)
        flash('Has añadido {} a favoritos'.format(name), 'info')

    db.session.commit()

    return make_response(redirect(url_for('details', name=name, pk=pk)))


@app.route('/lista/delete/', methods=['POST'])
@login_required
def delete_from_list():
    form = UpdateList(request.form)
    pk = form.data['pk']
    name = form.data['name']

    if form.validate_on_submit():
        products = Lista.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            accion = 'favorito',
            ).all()

        for favorite in products:
            db.session.delete(favorite)
            flash('Has eliminado {} de favoritos'.format(name), 'info')

        db.session.commit()

    return make_response(redirect(url_for('perfil')))
