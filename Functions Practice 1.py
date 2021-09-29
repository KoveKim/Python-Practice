# Function practice!
# A function is just a line of code that performs a specific task

# Functions start with a keyword. "def" is common
def greeting():  # The rest of the code in this function goes into the parantheses
    print("Hello!")

greeting()  # This is how you call the function


# You can pass information through a function
def greeting2(name):  # The parameter "name" gets defined when you call the function
    print("Hello", name)

greeting2("Khristian")  # You can pass any information to a parameter

# ---------------------------------------------

# Return statements

def cube(num):
    return num*num*num
    # We use return because the computer needs to return the answer
    # Return statements should be the last line of code in a function
    # because they will break the function at that line. For example:
    print("Hello world!")  # This doesn't get processed because of the return statement


print(cube(3))

result = cube(4)
print(result)
