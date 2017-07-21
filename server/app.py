from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from werkzeug.security import safe_str_cmp
from pony.orm import db_session, exists, commit
from server.model import User

from .api.account import account
from .api.image import image

# @db_session
# def get_user():
#   momo = User.get(id=5)
#   print(momo.display_name)

# get_user()

# def authenticate(display_name, password):
#   user = User.get(display_name=display_name)
#   return user.describe()
#   if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
#     return user;

# def identity(payload):
#   user_id = payload["identity"]
#   return User.get(id=5).describe()
#   return User.get(id=user_id).descibe()

app=Flask(__name__)
app.config['SECRET_KEY'] = "super-secret"

CORS(app)
jwt = JWTManager(app)

app.register_blueprint(account)
app.register_blueprint(image)