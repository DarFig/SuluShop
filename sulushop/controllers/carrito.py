from sulushop import app
from flask import request
from flask import render_template

from ..views import mysql
from ..util import *


@app.route('/carrito/', methods = ['GET',])
@login_required
def cart(buy=False):
    cur = mysql.connection.cursor()
    string = '''SELECT producto.nombre, SUM(producto.precio * carro.cantidad),
                        carro.cantidad, producto.id
                FROM carro
                LEFT JOIN producto on carro.id_producto = producto.id
                WHERE carro.id_usuario = {}
                GROUP BY producto.id
            '''.format(int(get_user_id()))
    cur.execute(string)
    summary = cur.fetchall()
    data = map(list, summary)

    for producto in data:
        pictures = get_product_cover(producto[3])
        if pictures:
            producto.append(pictures)

    return render_template('_views/carrito.html', productos=data)
# buy = request.args.get('buy', buy)
    # return render_template("_views/carrito.html")
