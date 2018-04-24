while True:

    operand1 = -1
    operand2 = -1
    number = 0

    while True:
        number = input('Please input number1:')
        if number == 'q':
            break
        operand1 = int(number)
        if operand1 < 0:
            print('Please input a positive number')
        else:
            break

    if number == 'q':
        print('This program has finished.')
        break

    while True:
        number = input('Please input number2:')
        if number == 'q':
            break
        operand2 = int(number)
        if operand2 < 0:
            print('Please input a positive number')
        else:
            break

    if number == 'q':
        print('This program has finished.')
        break

    my_sum = operand1 + operand2
    print('The result of number1 plus number2 is :{}'.format(my_sum))
