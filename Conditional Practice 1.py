def max_num():
    num1 = input("First number: ")
    num2 = input("Second number: ")
    num3 = input("Third number: ")

    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)


max_num()
