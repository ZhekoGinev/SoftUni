def func_executor(*args):
    result = []
    for function in args:
        result.append(function[0](*function[1]))
    return result
