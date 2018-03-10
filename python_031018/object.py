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
    super().__init__(name) # take the sound and add it to my parent
  def woof (self):
    print(self.sound)

class Dog (Animal):
  def __init__ (self, sound, *args): # '*args' suck everything up and passing them through, except sound
    self.sound = sound
    super().__init__(*args) # take the sound and add it to my parent
  def woof (self):
    print(self.sound)
# Remember we can use the debugging tools to find out what's going wrong.


class Robot:
  def auto_destruct (self):
    print("Boom!")
class RoboCat (Robot, Cat):
pass
class RoboDog (Robot, Dog):
  pass
 rcat = RobCat ('mittens')
 rcat.meow()
 rcat.auto_destruct()