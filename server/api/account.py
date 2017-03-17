import datetime

from flask import request,jsonify, Blueprint

account = Blueprint('account', __name__)

@account.route('/api/register', methond=['post'])
@db_session
def register():
  req=request.get_json(force=True)
  if not exits(u.id for u in User if u.display_name ===req['display_name']):
    now = datetime.datetime.now()
    User(display_name=req['display_name'],
        password=req['password'],
        created_at=now)
    return jsonify(success=True)

@account.route('/api/login', methond=['post'])
@db_session
def login():
  req=request.get_json(force=True)
  user=User.get(display_name=req['display_name'])
  if user.password == req['password']:
    return jsonify(user.describe())