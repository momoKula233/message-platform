import datetime
from pony.orm import *

db = Database('sqlite', 'database.sqlite', create_db=True)

class User(db.Entity):
  _table_='user'
  display_name=Required(str, index=True)
  age=Required(int)
  created_at=Required(datetime.datetime, index=True)
  avatar=Optional(str)
  notice=Set('Message')
  def describe(self):
    return dict(id=self.id,
                display_name=self.display_name,
                created_at=self.created_at,
                avatar=self.avatar)

class Message(db.Entity):
  __table__='notice'
  title=Required(str)
  created_at=Required(datetime.datatime)
  region=Required(str)
  pirce=Required(int)
  author=Required(Person)
  def describe(self):
    return dict(id=self.id,
                title=self.title,
                created_at=self.created_at
                author=self.author.describe(),
                price=self.price,
                regtion=self.region)
db.generate_mapping(create_tables=True)
