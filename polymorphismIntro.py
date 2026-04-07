class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!", end = " ")

  def printBrandModel(self):
    print(self.brand, self.model)

  def by(self):
    print("by Road")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def printBrandModel(self):
    print(self.brand, self.model)

  def move(self):
    print("Sail!", end = " ")
 
  def by(self):
    print("by Sea")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def printBrandModel(self):
    print(self.brand, self.model)

  def move(self):
    print("Fly!", end = " ")

  def by(self):
   print("by Air")

car1 = Car("Vigo", "2016")       #Create a Car object
boat1 = Boat("Kashti", "1965")               #Create a Boat object
plane1 = Plane("Aeroplane", "C-130")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
  x.printBrandModel()
  x.by()
