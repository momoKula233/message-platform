class Config:
  DEBUG = False
  DB_TYPE = 'sqlite'
  DB_PATH = None

class Development(Config):
  DEBUG = True
  DB_PATH = 'database.db'
