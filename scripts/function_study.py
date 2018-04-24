def get_a_number(_index=1):
    while True:
        number = input('please input number{}'.format(_index))
        if number == 'q':
            return -1
        operand = int(number)
        if operand < 0:
            print('Please input a positive number')
        else:
            return operand


def validate_number(_number):
    if _number == -1:
        print('You have quit this program')
        exit()


while True:
    operand1 = get_a_number()
    validate_number(operand1)

    operand2 = get_a_number(2)
    validate_number(operand2)

    my_sum = operand1 + operand2
    print('The result of number1 plus number2 is :{}'.format(my_sum))

