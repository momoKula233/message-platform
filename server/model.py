import datetime
from pony.orm import *

db = Database('sqlite', 'database.sqlite', create_db=True)

class User(db.Entity):
  _table_='user'
  display_name=Required(str, index=True)
  age=Optional(int)
  password=Optional(str)
  gender=Required(str)
  created_at=Required(datetime.datetime, index=True)
  avatar=Optional(str)
  notice=Set('Message')
  def describe(self):
    return dict(id=self.id,
                display_name=self.display_name,
                password=self.password,
                gender=self.gender,
                avatar=self.avatar)

class Message(db.Entity):
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
