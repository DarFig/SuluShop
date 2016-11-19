from sulushop import app
from flask import request
from flask import render_template

from ..views import mysql
from ..util import *


@app.route('/carrito/', methods = ['GET',])
@login_required
def cart(buy=False):
    cur = mysql.connection.cursor()
    string = '''SELECT * FROM carro WHERE id_usuario = {}
            '''.format(int(get_user_id()))
    cur.execute(string)
    summary = cur.fetchall()
    data = map(list, summary)

    return render_template('_views/carrito.html', productos=data)
    # buy = request.args.get('buy', buy)
    # return render_template("_views/carrito.html")
