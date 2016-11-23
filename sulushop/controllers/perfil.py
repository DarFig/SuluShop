from sulushop import app
from flask import request
from flask import render_template

from ..models import *
from ..views import *
from ..util import *
from favorito import UpdateList

@app.route('/deletUser/')
@login_required
def deletUser():
    data = get_user_cookie()
    usuario = get_user()
    db.session.delete(usuario)
    db.session.commit()
    #cur = mysql.connection.cursor()
    #cur.execute('''DELETE FROM usuario where email = %s
    #        ''', [data.get('userLogin[email]', ' ')] )
    #mysql.connection.commit()
    response = make_response(redirect(url_for('index')))
    data = {}
    response.set_cookie('character', json.dumps(data))
    return response


@app.route('/perfil/')
@login_required
def perfil():
    data = get_user_cookie()
    usuario = get_user()
    action=get_action_list()
    favorites=get_favorite_list()
    form = UpdateList()

    return render_template("_views/perfil.html", user=usuario, logueado=data,
            action=action, favorites=favorites, form=form)
