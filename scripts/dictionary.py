my_dict = {'Tom': 12, 'Jerry': 15, 'Sunny': 13}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for item in my_dict.items():
    print('{} is {} years old'.format(item[0], item[1]))
    key = item[0]
    value = my_dict[key]

del my_dict['Tom']
print(my_dict)

keys = ['Tom', 'Jerry', 'Sunny']
second_dict = dict.fromkeys(keys, 12)
print(second_dict)

