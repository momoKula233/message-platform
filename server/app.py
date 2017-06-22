from flask import Flask
from flask_cors import CORS

from .api.account import account
from .api.image import image

app=Flask(__name__)
CORS(app)

app.register_blueprint(account)
app.register_blueprint(image)