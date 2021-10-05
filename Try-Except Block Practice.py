# Try/Except Block practice

try:
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print(err)  # Print the error itself

except ValueError:
    print("Invalid input, numbers only")

# "Except" will catch ANY error in "try" under the sun and is too broad
# It's best to specify the error to catch in "except", as shown above
