#Ejecutalo y después probá cambiar el valor de age a 15 y luego a 8 para ver cómo cambia el resultado.
age = 20

# if / elif / else - the code makes decisions based on conditions
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

name = "Ignacio"
age = 34
city = "Byron"
height = 1.75

# f-string + conditionals combined
if height >= 1.80:
    height_comment = "you are tall"
elif height >= 1.70:
    height_comment = "you are average height"
else:
    height_comment = "you are short"

print(f"Hi, my name is {name}, I am {age} years old, I live in {city} and {height_comment}") #Hi, my name is Ignacio, I am 34 years old, I live in Byron and you are average height

# nested conditionals - conditionals inside conditionals
is_raining = False
has_umbrella = True

if is_raining:
    if has_umbrella:
        print("It's raining but you have an umbrella, you're fine")
    else:
        print("It's raining and you don't have an umbrella, you'll get wet")
else:
    print("It's not raining, enjoy the day")