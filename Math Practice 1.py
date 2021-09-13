from math import * #This imports math functions into your script

# Numbers are always INTEGERS
# You cannot combine integers with strings, but you can convert integers into strings
# You can also index a string which will output an integer

print(3 + 4.5)
print(-2.43) # Negative numbers work just fine
print(3 * (4 * 5)) # You must specify the operation. Operators: +, -, *, /, and %
print(10 % 3, "\n") # Modular. It outputs the remainder of the division equation.

num1 = 5
print(num1)
print(abs(num1)) # Absolute value is abs()
print(pow(num1, 5)) # Power of a number. This here is 5^5
print(max(2, 4, num1, 8, 10)) # Maximum, returns the number with highest value
print(min(1, 3, num1, 6, 10)) # Minimum, returns the number with lowest value
print(round(3.5), "\n") # Round a number to the nearest whole number.

print(floor(3.7)) # Rounds down, e.g. chops off decimal
print(ceil(3.2)) # Rounds up
print(sqrt(9)) # Square root
