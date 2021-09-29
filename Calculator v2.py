# Calculator v2

print("Program starting...\n")

num1 = float(input("First number: "))
op = input("Operator?: ")
num2 = float(input("Second number: "))

if op == "+":  # Add
    print(num1 + num2)
elif op == "-":  # Subtract
    print(num1 - num2)
elif op == "/":  # Divide
    print(num1 / num2)
elif op == "*":  # Multiply
    print(num1 * num2)
elif op == "%":  # Mod
    print(num1 % num2)
else:
    print("Please try again. Enter operator as symbol. Numbers only.")
