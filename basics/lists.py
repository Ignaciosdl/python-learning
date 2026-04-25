# creating a list
fruits = ["apple", "banana", "orange", "grape"]

# accessing elements by index (starts at 0)
print(fruits[0])   # first element
print(fruits[1])   # second element
print(fruits[-1])  # last element
print(fruits[-2])  # second to last element

# length of a list
print(len(fruits))

# modifying a list
fruits.append("mango")      # adds element at the end -> fruits = ["apple", "banana", "orange", "grape", "mango"]
fruits.insert(1, "lemon")   # adds element at index 1 -> fruits = ["apple", "lemon","banana", "orange", "grape", "mango"]
fruits.remove("banana")     # removes element by value -> fruits = ["apple", "lemon", "orange", "grape", "mango"]
fruits.pop()                # removes last element -> fruits = ["apple", "lemon", "orange", "grape"]

print(fruits)

# looping over a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
        
# slicing - extracting parts of a list: list[start:stop:step]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0:3])   # from index 0 to 2 -> numbers = [1, 2, 3]
print(numbers[3:7])   # from index 3 to 6 -> numbers = [4, 5, 6, 7]
print(numbers[:4])    # from start to index 3 -> numbers = [1, 2, 3, 4]
print(numbers[6:])    # from index 6 to end -> numbers = [7, 8, 9, 10]
print(numbers[::2])   # every 2 elements -> numbers = [1, 3, 5, 7, 9] 

print(numbers[::-1])  # reverses the list