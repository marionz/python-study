operand1 = -1
guess = True
while guess:
    number = input('please input the first number: ')
    operand1 = int(number)
    if operand1 < 0:
        print('please input a positive number')
    else:
        guess = False


operand2 = -1
guess = True
while guess:
    number = input('please input the second number: ')
    operand2 = int(number)
    if operand2 < 0:
        print('please input a positive number')
    else:
        guess = False

print(operand1, operand2)
