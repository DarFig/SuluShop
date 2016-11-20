import json
from functools import wraps
from flask import request, redirect, url_for

from models import *


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_user_cookie():
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if get_user_cookie():
            return redirect(url_for('perfil', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def get_user_cookie():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


def get_user_id():
    e_mail = get_user_cookie()['userLogin[email]']

    user = Usuario.query.filter_by(email=e_mail).first()

    return user.id


def get_user():
    e_mail = get_user_cookie()['userLogin[email]']

    user = Usuario.query.filter_by(email=e_mail).first()

    return user


def get_product_pictures(pk):
    picture = Foto.query.join(FotoProducto).filter(
            FotoProducto.id_producto == pk,
            FotoProducto.id_foto == Foto.id
            ).all()

    if not picture:
        return []

    return picture


def get_product_cover(pk):
    picture = Foto.query.join(FotoProducto).filter(
            FotoProducto.id_producto == pk,
            FotoProducto.id_foto == Foto.id,
            ).first()

    if not picture:
        return []

    return picture.url


def get_action_list():
    actions = Lista.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            ).all()

    return actions


def get_favorite_list():
    favorites = Lista.query.filter_by(
            id_usuario = get_user_id(),
            id_producto = pk,
            accion = 'favorito',
            ).all()

    return favorites
