from my_python import module

try:
    number1 = module.get_a_number(1)
    module.validate_number(number1)
    number2 = module.get_a_number(2)
    module.validate_number(number2)
    result = number1 + number2
    print(result)
except KeyboardInterrupt:
    print('You have quit this program.')
except EOFError:
    print('You end of this program')