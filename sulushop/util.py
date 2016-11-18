import json
from functools import wraps
from flask import request, redirect, url_for

from views import mysql


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
    email = get_user_cookie()['userLogin[email]']

    cur = mysql.connection.cursor()
    cur.execute('''SELECT id FROM usuario WHERE email = %s''', [email])
    summary = cur.fetchall()
    data = map(list, summary)

    return data[0][0]
