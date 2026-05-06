class Car:
    
    def __init__(self, brand, model, year): # Constructor method to initialize new objects
        self.brand = brand # Instance attribute (unique to each object)
        self.model = model # Instance attribute (unique to each object)
        self.year = year # Instance attribute (unique to each object)
        
    def display(self): # Instance method (action the object can perform)
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}") # result of the action 

car1 = Car("Mitsubishi", "Outlander", 2009) # create an object of the class Car (instantiate an object)
car2 = Car("Toyota", "Hiace", 2020) # create an object of the class Car (instantiate an object)

car1.display() # calling the action of that object
car2.display() # calling the action of that object