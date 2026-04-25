# defining a function
def greet():
    print("Hello, how are you?")

# calling the function
greet()
greet()
greet()

# function with parameters - you can pass information to the function
def greet(name):
    print(f"Hello {name}, how are you?")

greet("Ignacio")
greet("Maria")
greet("Juan")

# function with multiple parameters
def greet(name, age, city):
    print(f"Hello, my name is {name}, I am {age} years old and I live in {city}")

greet("Ignacio", 34, "Byron")
greet("Maria", 25, "Buenos Aires")

# return - the function gives back a result
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
print(add(100, 200))

# default parameters - if no value is passed, uses the default
def greet(name, language="english"):
    if language == "english":
        print(f"Hello {name}!")
    elif language == "spanish":
        print(f"Hola {name}!")

greet("Ignacio")
greet("Ignacio", "spanish")