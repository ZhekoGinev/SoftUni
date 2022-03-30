number = float(input())
if number == 0:
    print("zero")
else:
    if 0 < abs(number) < 1:
        print("small", end=" ")
    elif abs(number) > 1_000_000:
        print("large", end=" ")
    if number > 0:
        print("positive")
    else:
        print("negative")
