def round_number(numbers: str):
    return [round(float(num)) for num in numbers.split()]


number_sequence = input()

print(round_number(number_sequence))
