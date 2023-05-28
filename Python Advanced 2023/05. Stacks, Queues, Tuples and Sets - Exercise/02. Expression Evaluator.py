from functools import reduce
from math import floor

expression = input().split()    # ['6', '3', '-', '2', '1', '*', '5', '/']

idx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
}

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        result = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        expression[0] = result
        idx = 0

    idx += 1

print(floor(int(expression[0])))