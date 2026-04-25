# 1-Necesito un imput "What is your name " y asignarlo a una variable name 
# 2- Necesito un imput "How old are you " y asignarlo a una variable age 
# 3- Necesito un print con f string para crear texto flexible con variables

def name_age():
    name = input("What is your name? ")
    while True:
        try:
            age = int(input("How old are you? "))
            print(f"Hello {name}, you are {age} years old")
            break
        except ValueError:
            print("Please enter a valid number")

name_age()

