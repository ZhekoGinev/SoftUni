first_num = int(input())
second_num = int(input())
third_num = int(input())


def add_and_subtract(x, y, z):

    def sum_numbers(x, y):
        sum = x + y
        return sum

    def subtract(sum, z):  # sum is a parameter
        result = sum - z
        return result

    result = subtract(sum_numbers(x, y), z)

    return result


print(add_and_subtract(first_num, second_num, third_num))
