import functools
print(functools.reduce(lambda sum, elem: sum + elem, [1, 2, 3, 4, 5],0))

