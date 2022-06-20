from collections import defaultdict

numbers_count = defaultdict(int)

numbers = (float(i) for i in input().split())

for number in numbers:
    numbers_count[number] += 1

for num, count in numbers_count.items():
    print(f"{num:.1f} - {count} times")
