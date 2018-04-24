import sys
import method

assert len(sys.argv) == 3
a = int(sys.argv[1])
b = int(sys.argv[2])
result = method.add(a, b)
print(result)
