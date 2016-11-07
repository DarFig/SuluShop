from sulushop import app
from flask import request
from flask import render_template


@app.route('/carrito/', methods = ['GET',])
def cart(buy=False):
    buy = request.args.get('buy', buy)
    return render_template("_views/carrito.html")
