# Challenge: Classes/Objects

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Hasrat", 21)
p1.greet() 