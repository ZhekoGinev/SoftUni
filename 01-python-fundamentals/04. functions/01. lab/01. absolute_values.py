values = input()


def absolute(array_of_values):
    absolute = [abs(float(i)) for i in array_of_values.split()]
    return absolute


print(absolute(values))
