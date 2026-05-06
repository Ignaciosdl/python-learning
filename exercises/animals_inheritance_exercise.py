# Exercise: Model zoo animals using multiple inheritance.
# Create three classes: Animal, Mammal and Bird.
# Animal has an eat() method, Mammal has a breastfeed() method, Bird has a fly() method.
# Create a Bat class that inherits from Mammal and Bird (in that order).
# Bat should be able to eat(), breastfeed() and fly().
# Test changing the inheritance order and observe how MRO changes.

class Animal: 
    def eat(self): # Method (action the object can perform)
        print("eat") 

class Mammal(Animal): # Inherits all the atributes an methods of Animal
    def breastfeed(self): # Method (action the object can perform)
        print("breastfeed")

class Bird(Animal): # Inherits all the atributes an methods of Animal
    def fly(self): # Method (action the object can perform)
        print("fly")

class Bat(Mammal, Bird): # Inherits all the attributes an methods of Mammal and Bird and also from Animal
    pass

bat = Bat() # Instance an object 

bat.eat() 
bat.breastfeed()
bat.fly()
print(Bat.mro()) # .mro() to show the herachy of inheritance