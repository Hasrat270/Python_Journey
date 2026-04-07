# Instructions
# Inside the editor, complete the following steps:
# 1. Create a class called Rectangle
# 2. Add an __init__ method with width and height, and store them as properties
# 3. Add a method called area that returns the width multiplied by the height
# 4. Create an object r1 with width 5 and height 3
# 5. Print the area of r1

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def area(self):
    return self.width * self.height

r1 = Rectangle(5,3)
print(r1.area())