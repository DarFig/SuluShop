from sulushop import app
from flask import request
from flask import render_template

from ..models import *
from ..views import *
from ..util import *
from lista import UpdateList


@app.route('/deletUser/')
@login_required
def deletUser():
    data = get_user_cookie()
    usuario = get_user()
    db.session.delete(usuario)
    db.session.commit()
    response = make_response(redirect(url_for('index')))
    data = {}
    response.set_cookie('character', json.dumps(data))
    return response


@app.route('/perfil/', methods=['GET'])
@login_required
def perfil():
    data = get_user_cookie()
    usuario = get_user()
    action=get_action_list()
    favorites=get_favorite_list()
    form = UpdateList()

    return render_template("_views/perfil.html", user=usuario, logueado=data,
            action=action, favorites=favorites, form=form)

@app.route('/mod_datos/', methods=['GET', 'POST'])
@login_required
def mod_datos():
    if request.method == 'GET' :
        usuario = get_user()
        data = get_user_cookie()
        return render_template("_modules/modificar.html", saves=data, user=usuario)
    else :
        data = get_user_cookie()
    	data.update(dict(request.form.items()))
        usuario = get_user()
        db.session.delete(usuario)
    	usuario.nombre = data.get('userLogin[nombre]', ' ')
    	usuario.apellidos = data.get('userLogin[apellidos]', ' ')
    	usuario.fecha_nacimiento = data.get('userLogin[nacimiento]', ' ')
    	usuario.direccion = data.get('userLogin[direccion]', ' ')
    	usuario.email = data.get('userLogin[email]', ' ')
    	usuario.telefono = data.get('userLogin[telefono]', ' ')
        db.session.add(usuario)
        db.session.commit()

        action=get_action_list()
        favorites=get_favorite_list()
        form = UpdateList()

        return render_template("_views/perfil.html", user=usuario, logueado=data,
                action=action, favorites=favorites, form=form)
