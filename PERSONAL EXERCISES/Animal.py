class Animal():
  def __init__(self):
    pass
  def sound(self,animal_sound):
    return f"This Animal {animal_sound}"
  
class Characteristic():  
  def __init__(self):
    pass
  def legs(self, animal_character):
    return f"This Animal has {animal_character} legs"  

class Dog(Animal,Characteristic):
  pass

class Cat(Animal,Characteristic):
  pass
class Kangaroo(Animal,Characteristic):
  pass
  

tiger=Dog()
kitty=Cat()
Bob=Kangaroo()
print(tiger.sound("barks"),tiger.legs("four"))
print(kitty.sound("Meow"),kitty.legs("four"))
print(Bob.sound("Growl"),kitty.legs("Two"))
