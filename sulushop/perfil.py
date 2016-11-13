from sulushop import app
from flask import request
from flask import render_template

@app.route('/perfil/')
def perfil():
    return render_template("_views/perfil.html")