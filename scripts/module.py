from my_python import log_util
import logging

__desc__ = 'this is my first module'

log_util.setup_log_and_return_log_file()


def get_a_number(_index=1):
    while True:
        number = input('please input number{}:'.format(_index))
        if number == 'q':
            return -1
        try:
            operand = int(number)
            if operand < 0:
                print('Please input a positive number')
                logging.warning('User have input a negative number \'{}\'.'.format(number))
            else:
                return operand
        except ValueError:
            print('Please input an integer:')
            logging.error('User have input an invalid string \'{}\'.'.format(number))
        else:
            print('There is no exception')
        finally:
            print('You will always come here')


def validate_number(_number):
    if _number == -1:
        print('You have quit this program')
        logging.info('User chose quit the program.')
        exit()
