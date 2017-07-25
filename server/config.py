from datetime import timedelta

class DefaultConfig(object):
  DEBUG = True
  JWT_SECRET_KEY = 'secret'
  JWT_EXPIRATION_DELTA = timedelta(seconds=31556926)