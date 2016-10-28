from sulushop import app
from flask import request
from flask import render_template

@app.route('/')
def index():
    return render_template("_modules/lista.html");
