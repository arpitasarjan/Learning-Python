from functools import reduce

# List
l = [1, 2, 3, 4, 5, 6]

# Even number function
def even(n):
    return n % 2 == 0

# Filter example
onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce example
def sum(a, b):
    return a + b

mul = lambda x, y: x * y

print(reduce(sum, l))
print(reduce(mul, l))
