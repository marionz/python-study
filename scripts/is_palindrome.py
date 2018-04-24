def reverse(_source):
    new_string = _source[::-1]
    return new_string


def is_palindrome(_source):
    new_string = reverse(_source)
    if _source == new_string:
        return True
    else:
        return False


while True:
    string = input('Please input a string:\n')
    if is_palindrome(string):
        print('This is a palindrome')
        break
    else:
        print('This is not a palindrome')
