numbers = input()


def sort_sequence(sequence: str):
    sequence = [int(i) for i in sequence.split()]
    sorted_list = sorted(sequence)
    return sorted_list


print(sort_sequence(numbers))
