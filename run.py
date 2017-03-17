from pony.orm import *

db = Database('sqlite', 'test_db.sqlite', create_db=True)
class Person(db.Entity):
  name = Required(str)
  age = Required(int)
  cars = Set("Car")

class Car(db.Entity):
  make = Required(str)
  model = Required(str)
  owner = Required(Person)
db.generate_mapping(create_tables=True)

@db_session
def create_entities():
  p1 = Person(name='Peter', age=20)
  c1 = Car(make='Toyota', model='Prius', owner=p1)

create_entities()