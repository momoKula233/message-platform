import datetime
from pony.orm import *

db = Database('sqlite', 'database.sqlite', create_db=True)

class User(db.Entity):
  _table_='user'
  username=Required(str, index=True)
  age=Optional(int)
  password=Required(str)
  user_id=Required(datetime.datetime, index=True)
  gender=Required(str)
  created_at=Required(datetime.datetime, index=True)
  avatar=Optional(str)
  notices=Set('Notice')
  def describe(self):
    return dict(id=self.id,
                username=self.username,
                age=self.age,
                gender=self.gender,
                avatar=self.avatar)

class Notice(db.Entity):
  __table__='notice'
  title=Required(str)
  created_at=Required(datetime.datetime)
  region=Required(str)
  pirce=Required(int)
  author=Required(User)
  def describe(self):
    return dict(id=self.id,
                title=self.title,
                created_at=self.created_at,
                author=self.author.describe(),
                price=self.price,
                regtion=self.region)
db.generate_mapping(create_tables=True)
