# for loop - repeats a fixed number of times (from 0 to range number -1)
for i in range(5):
    print(i)
    
# range(start, stop) - start is inclusive, stop is exclusive
for i in range(1, 6):
    print(i)
    
# looping over a list of items
fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(fruit)

# while loop - repeats while a condition is True
counter = 0

while counter < 5:
    print(counter)
    counter += 1  # counter = counter + 1
    
# break - stops the loop completely
print("--- break ---")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skips current iteration and continues
print("--- continue ---")
for i in range(10):
    if i == 5:
        continue
    print(i)