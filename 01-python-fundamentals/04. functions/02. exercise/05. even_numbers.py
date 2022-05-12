numbers = input()


def evens(sequence):
    sequence = [int(i) for i in sequence.split()]
    evens = list(filter(lambda x: x % 2 == 0, sequence))
    return evens


print(evens(numbers))
