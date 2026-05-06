# Exercise: Create a Student class with name, age and grade attributes
# and a study() method. Interact with the user to get the attributes.

class Student:
    def __init__(self, name, age, grade): # Constructor method to initialize new objects
        self.name = name
        self.age = age
        self.grade = grade
    
    def estudiar(self): # Instance method (action the object can perform)
        print(f"The student {self.name} is studing")

def students(): # function tu instance objects
    name = input("What is your name? ")
    age = input("How old are you? ")
    grade = input("What is your grade? ")
    student = Student(name, age, grade)
    return student

student1 = students() # Instantiate an object

def action_to_do(student):
    action = input("What do you want to do? ").lower()
    if action == "study":
        student.estudiar()
    else:
        print(f"You have chosen {action} instead of study")

action_to_do(student1)