from functools import reduce


def operate(*args):
    data = list(args)
    op = data.pop(0)

    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    return reduce(operators[op], data)
