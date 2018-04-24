string = """
this is a string.
I will write it to a file first,
then I will read it later.
"""

file = open('data.txt', 'w')
file.write(string)
file.close()

strings = ['item1\n', 'item2\n', 'item3\n']
file = open('data.txt', 'a')
file.writelines(strings)
file.close()

file = open('data.txt', 'r')
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end='')
file.close()
