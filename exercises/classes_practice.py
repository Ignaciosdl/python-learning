class Car:
    
    def __init__(self, brand, model, year): # constractor of the class
        self.brand = brand # atributes of the class
        self.model = model # atributes of the class
        self.year = year # atributes of the class
        
    def display(self): # creating a function/action of the class
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}") # result of the action 

car1 = Car("Mitsubishi", "Outlander", 2009) # create an object of the class Car
car2 = Car("Toyota", "Hiace", 2020) # create an object of the class Car

car1.display() # calling the action of that object
car2.display() # calling the action of that object