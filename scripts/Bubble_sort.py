def bubble_sort(_source):

    length = len(_source)

    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if _source[j] > _source[j+1]:
                (_source[j], _source[j+1]) = (_source[j+1], _source[j])
