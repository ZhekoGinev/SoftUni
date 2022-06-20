# This ugly piece of code actually works for the given problem.
# I'd rather not waste anymore hours on it, trying to come up with a better approach.


def subtract(array: list):
    result = array.pop(0)
    for i in array:
        result -= i
    return result


def multiply(array: list):
    result = array.pop(0)
    for i in array:
        result *= i
    return result


def divide(array: list):
    result = array.pop(0)
    for i in array:
        result //= i
    return result


# converting numbers from str to integer
expr = []
temp_expr = input().split()
for i in temp_expr:
    if i[-1].isdigit():  # in order to catch negative numbers (e.g. -1)
        expr.append(int(i))
    else:
        expr.append(i)

# creating a new list in which each expression is a separate element
expressions = []
temp = []
for ch in expr:
    if type(ch) == int:
        temp.append(ch)
    else:
        temp.append(ch)
        expressions.append(temp)
        temp = []


for i, x in enumerate(expressions):

    operator = x.pop()  # last element in each expression is the operator
    if operator == '-':
        # if we're not at the last index insert the result in the next element at index 0
        if expressions[i] != expressions[-1]:
            expressions[i+1].insert(0, subtract(x))
        else:
            # if it's the last index just append the result and break
            expressions = subtract(x)
            break
    elif operator == "+":
        if expressions[i] != expressions[-1]:
            expressions[i+1].insert(0, sum(x))
        else:
            expressions = sum(x)
            break
    elif operator == "*":
        if expressions[i] != expressions[-1]:
            expressions[i+1].insert(0, multiply(x))
        else:
            expressions = multiply(x)
            break
    elif operator == "/":
        if expressions[i] != expressions[-1]:
            expressions[i+1].insert(0, divide(x))
        else:
            expressions = divide(x)
            break

print(expressions)
