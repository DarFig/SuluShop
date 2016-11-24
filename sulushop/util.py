from sulushop import login_manager
import json
from flask import request

from models import *


@login_manager.user_loader
def load_user(user_id):
        return Usuario.get(user_id)


def get_user_cookie():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


def get_user_id():
    e_mail = get_user_cookie()['email']

    user = Usuario.query.filter_by(email=e_mail).first()

    return user.id

def get_user_contrasena(e_mail):
    user = Usuario.query.filter_by(email=e_mail).first()
    return user.contrasena

def get_user():
    e_mail = get_user_cookie()['email']

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
    actions = Producto.query.join(Lista).filter(
            Lista.id_usuario == get_user_id()
            ).add_columns(Lista.fecha).all()

    return actions


def get_favorite_list():
    favorites = Producto.query.join(Lista).filter(
            Lista.id_usuario == get_user_id(),
            Lista.accion == 'favorito',
            ).add_columns(Lista.fecha).all()

    return favorites
