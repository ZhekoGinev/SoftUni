command = input()
numbers = input().split()


def sum_odd_or_even(command: str, numbers: list):
    if command == "Odd":
        sum_odds = sum([int(n) for n in numbers if int(n) % 2 != 0])
        final = sum_odds * len(numbers)
        return final
    elif command == "Even":
        sum_evens = sum([int(n) for n in numbers if int(n) % 2 == 0])
        final = sum_evens * len(numbers)
        return final


print(sum_odd_or_even(command, numbers))
