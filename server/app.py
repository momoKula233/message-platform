from flask import *
from flask_cors import CORS

from .api.user import user

app=Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(user)