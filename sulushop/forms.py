from wtforms import Form
from wtforms import StringField, TextFiel
from wtforms.fields.html5 import EmailField

class loginForm(Form):
    email = StringField('username')
    password = EmailField('email')
