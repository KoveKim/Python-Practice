# Exponent function practice

print(2**3)  # 2^3
print(2^3)  # This is not the exponent operator

def exponent(base, power):
    result = 1  # Store the result of the math

    for index in range(power):  # Loop is based on the value of the power
        result = result * base
    return result


print(exponent(3, 3))
