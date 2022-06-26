# it's a rather ugly solution but it works fine so I'm not touching it

from math import ceil

numbers = [int(num) for num in input().split(", ") if int(num) >= 0]
groups = []

# construct list with empty groups based on the highest number
# it's necessary to round up with ceil
for num in range(ceil(max(numbers) / 10)):
    groups.append([])

# check each number and append to the proper group
for index, number in enumerate(numbers):
    for i in range(1, len(groups) + 1):
        if number <= i * 10:  # using indices as if they're 10, 20, 30 etc.
            groups[i - 1].append(number)
            break

for index, group in enumerate(groups):
    print(f"Group of {index + 1}0's: {group}")
