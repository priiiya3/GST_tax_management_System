from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask import Response, redirect
from werkzeug.exceptions import HTTPException
from flask_admin.contrib.sqla import ModelView
from Project.AES import AESCipher

app = Flask("Project")
app.config['SECRET_KEY'] = 'secrekey%$##387723232Fda7s9as5da3sad69292uj3m3n4363n33i8dd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

AES_Key = b"c80825a438f9uird"

db = SQLAlchemy(app)
Basic_auth = BasicAuth(app)


def encryption(data):
    Pass = AESCipher(AES_Key).Encrypt(bytes(str(data).encode('utf-8')))
    Pass = (str(Pass).replace("'", "")[1:])
    return str(Pass)


def decryption(data):
    Pass = AESCipher(AES_Key).Decrypt(bytes(data.encode('utf-8')))
    return str(Pass)


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "Authentication Failed. Please reload the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class CustomModelView(ModelView):
    def is_accessible(self):
        if not Basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(Basic_auth.challenge())


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if not Basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(Basic_auth.challenge())


App_Admin = Admin(app, index_view=CustomAdminIndexView())

from Project import auth
from Project import main
from Project import Process_Routs
from Project.models import User, TaxPayer, Tax

App_Admin.add_view(CustomModelView(User, db.session))
App_Admin.add_view(CustomModelView(TaxPayer, db.session))
App_Admin.add_view(CustomModelView(Tax, db.session))

db.create_all()
db.session.commit()
