from server.model import User

def authenicate(username, password):
  user = User.find_by_username(username)
  return user

def identity(payload):
  user_id = payload['identity']
  return User.find_by_id(user_id)