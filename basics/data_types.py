# str - text, always inside quotes
name = "Ignacio"

# int - whole numbers
age = 34

# float - decimal numbers
height = 1.75

# bool - only True or False
is_programmer = True

# you can check the type of any variable with type()
print(type(name))
print(type(age))
print(type(height))
print(type(is_programmer))

# type conversion - converting one type to another
age_text = str(age)       # int to str
height_int = int(height)  # float to int (removes decimals)
age_float = float(age)    # int to float

print(type(age_text))
print(type(height_int))
print(type(age_float))

print(height_int)   # see what happens to the decimals
print(age_float)    # see how int becomes float