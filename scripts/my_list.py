class MyList:

    def __init__(self):
        self.my_list = list()

    def __getitem__(self, _index):
        return self.my_list[_index]

    def __str__(self):
        return 'I am an object of class MyClass, I have a field called my_list' \
               ' and it has {} item(s).'.format(len(self))

    def __len__(self):
        return len(self.my_list)

    def add(self, _object):
        self.my_list.append(_object)

    def remove(self, _object):
        self.my_list.remove(_object)


if __name__ == '__main__':

    my_list = [4, 3, 1, 3, 2, 5]
    print(my_list)

    my_list.append(6)
    print(my_list)

    my_list.insert(2, 7)
    print(my_list)

    my_list.remove(1)
    print(my_list)

    removed_number = my_list.pop(2)
    print(removed_number)
    print(my_list)

    my_list.sort()
    print(my_list)

    my_list.reverse()
    print(my_list)

    new_list = [9, 10]
    my_list.extend(new_list)
    print(my_list)

    my_index = my_list.index(9)
    print(my_index)

    occurrences_of_3 = my_list.count(3)
    print(occurrences_of_3)

    your_list = my_list.copy()
    print(your_list)
    print(my_list)

    his_list = your_list
    your_list.clear()
    print(your_list)
    print(my_list)
    print(his_list)

    my_tuple = tuple(my_list)
    print(my_tuple)
    a = my_tuple[2]
    print(a)

    length_of_my_tuple = len(my_tuple)
    print(length_of_my_tuple)





