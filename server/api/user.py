import json

from flask import request, jsonify, Blueprint
from pony.orm import db_session, commit
from pony.orm.serialization import json_converter

from server.model import User

user = Blueprint('user', __name__)

@user.route('/user/u<int: id>')
@db_session
def get_user(id):
  user=User.get(id)
  return json.dumps(user.describe(), default=json_converter)


@user.route('/user/u<int: id>', methonds=['post'])
@db_session
def update_user(id):
  user=User.get(id=id)
  req=request.get_json(force=True)
  user.dispay_name=req['dispay_name']
  user.avatar=req['avatar']
  return jsonify(success=True)
