from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sulushop:1234sulushop@localhost/sulushop"


db = SQLAlchemy(app)

import sulushop.views
