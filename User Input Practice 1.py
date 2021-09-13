print("Program starting...")

# name = input("Enter your name: ") # input() calls for the user to input some sort of value
# User input will be stored in the variable "name"
# print("Hello ", name, "!")

# Now, we're going to make a calculator.
num1 = input()
num2 = input("+ ")
# result = int(num1) + int(num2) # Must specify int() function for all strings
result = float(num1) + float(num2)
# Remember, Python converts user input into a string.
print("=", result)

# int() will only return whole numbers. You must use float() for decimals to work.
# They are both situational, but for the purpose of a calculator, we want decimals to work.
