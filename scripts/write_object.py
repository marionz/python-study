# encoding=utf-8
import io
import pickle

var = ['张磊', '马明明', '안녕']
file = io.open('data.txt', 'w+b')
pickle.dump(var, file)
file.close()

file = io.open('data.txt', 'rb')
strings = pickle.load(file)
print(strings[0])
file.close()
