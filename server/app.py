from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from werkzeug.security import safe_str_cmp
from pony.orm import db_session, exists, commit
from server.model import User
from server.config import DefaultConfig

from .api.account import account
from .api.image import image


app=Flask(__name__, static_folder='./images/', static_url_path='/static')
# app.config['SECRET_KEY'] = "super-secret"
app.config.from_object(DefaultConfig)

CORS(app)
jwt = JWTManager(app)

app.register_blueprint(account)
app.register_blueprint(image)