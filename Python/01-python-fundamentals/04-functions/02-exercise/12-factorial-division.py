from math import factorial

first_num = int(input())
second_num = int(input())


def factorial_division(a, b):

    return factorial(a) / factorial(b)


result = factorial_division(first_num, second_num)
print(f"{result:.2f}")