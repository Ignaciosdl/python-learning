# Exercise: Create a school system with two classes: Person and Student.
# Person class has name and age attributes and a method to print them.
# Student class inherits from Person, adds a grade attribute and a method to print it.
# Use super() in __init__ to reuse Person's code.
# Create a Student instance and test all attributes and methods.

class Person: # Class person with atributes and methonds
    def __init__(self, name, age): # Constructor method to initialize new objects
        self.name = name
        self.age = age
        
    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person): # inherits from Person
    def __init__(self, name, age, grade):
        super().__init__(name, age)# reutilize the __init__ from Person
        self.grade = grade  # add the new atribute from Student
    
    def show_grade(self): 
        print(f"Grade: {self.grade}")

student1 = Student("Ignacio", 34, 6) # Instantiate an object

student1.show_data() # Call the methods
student1.show_grade()