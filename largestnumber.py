number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 >= number3:
    print("The largest number is", number1)
elif number2 > number1 >= number3:
    print("The largest number is", number2)
elif number3 > number1 >= number2:
    print("The largest number is", number3)

