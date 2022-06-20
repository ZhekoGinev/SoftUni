MIN_NUM = 1
MAX_NUM = 100
while True:
    number = float(input())
    if MIN_NUM <= number <= MAX_NUM:
        break
print(f"The number {number} is between {MIN_NUM} and {MAX_NUM}")
