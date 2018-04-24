import sys


def add(a, b):
    return a + b


def my_print():
    print('my print')


if __name__ == '__main__':
    print(my_print())

    print(sys.argv)

    add1 = add(int(sys.argv[1]), int(sys.argv[2]))
    print(add1)
