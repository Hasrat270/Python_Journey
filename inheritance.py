# Challenge: Inheritance

class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print(self.name)

class Dog(Animal):
  pass # kuch naya nahi kr rahe add isliye pass

d1 = Dog("Rex")
d1.speak()