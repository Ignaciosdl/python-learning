name = "Ignacio"
age = 34
city = "Byron"

print(name)
print(age)
print(city)

#print("My name is " + name + ", I am " + str(age) + " years old an I live in " + city)
# f-string: cleaner and modern way to combine variables with text
# no need for str() or +, just put variables inside {}
print(f"My name is {name}, I am {age} years old an I live in {city}")