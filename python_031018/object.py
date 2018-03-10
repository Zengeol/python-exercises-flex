class Animal:
  def __init__ (self, name): # instructor; name is an attribute.
    self.name = name #Save the name to the object
    
class Dog (Animal): # let's take an animal
  def woof (self):
    print("Woof")
class Cat (Animal):
  def meow (self):
    print("Meow")
    
mittens = Cat('Mittens') # cat needs a name
farfel = Dog('Farfel')

# now we test them.
mittens.name
farfel.name
mittens.meow
mittens.farfel
farfel.woof

# Multy-level inferitance
class ShihTzu (Dog):
  def woof (self):
    print("Yip Yip")
    
dog1 = shihTzu("cofeeve")
dog1.woof() # we are overwriting the old

class Dog (Animal):
  def __init__ (self, name, sound):
    self.sound = sound
    super().__init__(name)
  def woof (self):
    print(self.sound)
