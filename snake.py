length = int(input("Enter the length of snake:  "))
snake = ""
for i in range(length):
    if i % 2 == 0:
        snake += "*"
    else:
        snake += "#"
print(snake)
