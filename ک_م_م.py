number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    greater = number1
else:
    greater = number2

for i in range(greater, number1 * number2 + 1):
    if i % number1 == 0 and i % number2 == 0:
        latest = i
        break

print("the Least common denominator of ",number1," and" ,number2, "is:",latest)