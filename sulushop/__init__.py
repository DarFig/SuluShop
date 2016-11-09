from flask import Flask
app = Flask(__name__)

app.config['MYSQL_USER'] = "sulushop"
app.config['MYSQL_PASSWORD'] = "1234sulushop"
app.config['MYSQL_DB'] = "sulushop"

import sulushop.views
