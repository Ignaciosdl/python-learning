# arithmetic operators
a = 10
b = 3

print(a + b)   # addition -> 13
print(a - b)   # subtraction -> 7
print(a * b)   # multiplication -> 30
print(a / b)   # division -> 3.333...
print(a // b)  # integer division (removes decimals) -> 3
print(a % b)   # modulo (remainder of division) -> 1
print(a ** b)  # exponentiation (a to the power of b) -> 1000

# comparison operators - always return True or False
print(a > b)   # greater than -> True
print(a < b)   # less than -> False
print(a == b)  # equal to -> False
print(a != b)  # not equal to -> True
print(a >= b)  # greater than or equal to -> True
print(a <= b)  # less than or equal to -> False

# logical operators - combine multiple comparisons
print(a > 5 and b > 5)   # True only if BOTH are True -> False
print(a > 5 or b > 5)    # True if AT LEAST ONE is True -> True
print(not a > 5)          # inverts the result -> False