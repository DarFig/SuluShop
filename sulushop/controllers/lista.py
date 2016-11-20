import datetime
from sulushop import app
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import url_for
from sqlalchemy.sql import func


from ..models import *
from ..util import *


@app.route('/lista/add/', methods = ['POST',])
@login_required
def add_to_list():
    pk = request.form['pk']
    date = datetime.datetime.utcnow()

    product = Lista('favorito', date, get_user_id(), pk)
    db.session.add(product)
    db.session.commit()
    # TODO: redirect to product detail
    return make_response(redirect(url_for('cart')))


@app.route('/lista/delete/', methods = ['POST',])
@login_required
def delete_from_list():
    pk = request.form['pk']

    products = Lista.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            accion = 'favorito',
            ).all()

    for favorite in products:
        db.session.delete(favorite)

    db.session.commit()
    # TODO: redirect to profile
    return make_response(redirect(url_for('cart')))
