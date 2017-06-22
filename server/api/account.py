from flask import request, jsonify, Blueprint
from pony.orm import db_session, exists, commit
from server.model import User
import datetime

account = Blueprint('account', __name__)


@account.route('/register', methods=['post'])
@db_session
def register():
    req = request.get_json()
    if not exists(u.id for u in User if u.display_name == req['display_name']):
        now = datetime.datetime.now()
        User(display_name=req['display_name'],
             gender=req['gender'],
             avatar=req['avatar'],
             age=req['age'],
             password=req['password'],
             created_at=now)
        user = User.get(display_name=req['display_name'])
        return jsonify(success=True, user=user.describe())
    else:
        return jsonify(success=False, err='INVAILD_USERNAME')


@account.route('/login', methods=['POST'])
@db_session
def login():
    req = request.get_json(force=True)
    print(req['display_name'])
    user = User.get(display_name=req['display_name'])
    if not user:
        return jsonify(success=False,err="INVAILD_USER")
    if user.password == req['password']:
        return jsonify(success=True, user=user.describe())
    else:
        return jsonify(success=False, err="INVAILD_PASSWORD")
