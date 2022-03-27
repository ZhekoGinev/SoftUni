data_array = input().split()
data_array = [int(i) for i in data_array]


def exchange(arr, index):
    if index < len(arr) and index >= 0:
        return arr[index+1:] + arr[:index + 1]
    else:
        return "Invalid index"


def max_even(arr):
    max_index = 0
    max_even = -2**31
    is_found = False
    for i, num in enumerate(arr):
        if num >= max_even and num % 2 == 0:
            max_even = num
            max_index = i
            is_found = True
    if is_found:
        return max_index
    else:
        return "No matches"


def max_odd(arr):
    max_index = 0
    max_odd = -2**31
    is_found = False
    for i, num in enumerate(arr):
        if num >= max_odd and num % 2 != 0:
            max_odd = num
            max_index = i
            is_found = True
    if is_found:
        return max_index
    else:
        return "No matches"


def min_even(arr):
    min_index = 0
    min_even = 2**31
    is_found = False
    for i, num in enumerate(arr):
        if num <= min_even and num % 2 == 0:
            min_even = num
            min_index = i
            is_found = True
    if is_found:
        return min_index
    else:
        return "No matches"


def min_odd(arr):
    min_index = 0
    min_odd = 2**31
    is_found = False
    for i, num in enumerate(arr):
        if num <= min_odd and num % 2 != 0:
            min_odd = num
            min_index = i
            is_found = True
    if is_found:
        return min_index
    else:
        return "No matches"


def count_first_even(arr, range_bound):
    result = []
    if range_bound > len(arr):
        return "Invalid count"
    else:
        for i in arr:
            if i % 2 == 0 and len(result) < range_bound:
                result.append(i)
        return result


def count_first_odd(arr, range_bound):
    result = []
    if range_bound > len(arr):
        return "Invalid count"
    else:
        for i in arr:
            if i % 2 != 0 and len(result) < range_bound:
                result.append(i)
        return result


def count_last_even(arr, range_bound):
    result = []
    if range_bound > len(arr):
        return "Invalid count"
    else:
        for i in reversed(arr):
            if i % 2 == 0 and len(result) < range_bound:
                result.insert(0, i)
        return result


def count_last_odd(arr, range_bound):
    result = []
    if range_bound > len(arr):
        return "Invalid count"
    else:
        for i in reversed(arr):
            if i % 2 != 0 and len(result) < range_bound:
                result.insert(0, i)
        return result


while True:
    command = input()
    if command == "end":
        break
    else:
        tokens = command.split()
        if tokens[0] == "exchange":
            temp = exchange(data_array, int(tokens[1]))
            error = "Invalid index"
            if temp != error:
                data_array = temp
            else:
                print(error)
        elif tokens[0] == "max":
            if tokens[1] == "even":
                print(max_even(data_array))
            else:
                print(max_odd(data_array))
        elif tokens[0] == "min":
            if tokens[1] == "even":
                print(min_even(data_array))
            else:
                print(min_odd(data_array))
        elif tokens[0] == "first":
            count = int(tokens[1])
            if tokens[2] == "even":
                print(count_first_even(data_array, count))
            else:
                print(count_first_odd(data_array, count))
        elif tokens[0] == "last":
            count = int(tokens[1])
            if tokens[2] == "even":
                print(count_last_even(data_array, count))
            else:
                print(count_last_odd(data_array, count))

print(data_array)
