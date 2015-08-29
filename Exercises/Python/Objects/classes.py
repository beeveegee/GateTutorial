#GateTutorial
#http://samolds.github.io/gate/guide/python.html#objects

#classes

from datetime import datetime

class Person():
  def __init__(self, name, birth_year, ethnicity = None):
    self.name = name
    self.birth_year = birth_year
    self.ethnicity = ethnicity

  def get_age(self):
    age = datetime.now().year - self.birth_year
    return age

john = Person("John",1990)

print john
print
print john.get_age()

#Get the age without a object
#can get age, but that's it

def x_get_age(birth_year):
  age = datetime.now().year - birth_year
  return age



print x_get_age(1990)
