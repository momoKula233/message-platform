from flask import request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from pony.orm import db_session, exists, commit, select, raw_sql, desc
from pony.orm.serialization import json_converter
from server.model import User, Notice

import datetime

message = Blueprint('message', __name__)

def serialize(items):
  return [p.describe() for p in items]

@message.route('/get_message_list')
@db_session
def get_messages():
  posts = select(p for p in Notice).order_by(desc(Notice.created_at))
  results = serialize(posts)
  return json.dumps(results, default=json_converter)

@message.route('/post_message', methods=['post'])
@db_session
@jwt_required
def add_message():
  current_id = get_jwt_identity()
  user = User.get(id=current_id)
  if not user:
    return (err='INVALID_AUTHORIZATION'), 401
  req = request.get_json()
  now = datetime.datetime.now()
  Notice(
    title=req['title'],
    region=req['region'],
    price=req['price'],
    user=user,
    created_at=now
  )
  return jsonify(success=False)

