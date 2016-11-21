from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from htmlmin.main import minify
from flask.ext.login import LoginManager
from flask.ext.gzip import Gzip


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
gzip = Gzip(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sulushop:1234sulushop@localhost/sulushop"


db = SQLAlchemy(app)


@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
            )

        return response
    return response


import sulushop.views
