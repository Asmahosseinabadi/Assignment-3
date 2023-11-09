number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

for i in range(min(number1, number2), 0, -1):
    if number1 % i == 0 and number2 % i == 0:
        print("the greatest common divisor of ",number1," and" ,number2, "is:",i)
        break