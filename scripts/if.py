operand = input('please enter your number: ')
number = int(operand)
print('The number you entered is {}'.format(number))
if number > 10:
    print('The number is greater than 10.')
elif number < 5:
    print('The number is less than 5.')
else:
    print('The number is less than 10 and greater than 5.')

