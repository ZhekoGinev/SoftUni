boundary = int(input())

for number in range(1, boundary + 1):
    numstring = str(number)
    sum = 0
    is_special = False
    for digit in numstring:
        sum += int(digit)
    if sum in (5, 7, 11):
        is_special = True
    print(f"{number} -> {is_special}")
