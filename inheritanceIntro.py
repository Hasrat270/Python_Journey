class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)
    
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationYear = year
    
x = Student("Hasrat","Khan",2020)
# print(x.firstname)
# print(x.lastname)
x.printname()
print(x.graduationYear)