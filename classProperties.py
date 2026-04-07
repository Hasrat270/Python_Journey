# Challenge: Class Properties
# Instructions
# 1. Inside the editor, complete the following steps:
# 2. Create a class Student with an __init__ that takes name and grade, and stores them as properties
# 3. Create an object s1 with name "Anna" and grade "A"
# 4. Print the grade of s1
# 5. Change the grade of s1 to "B"
# 6. Print the updated grade

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna","A")
print(s1.grade)
s1.grade = "B"
print(s1.grade)