# there's like 10 different ways to solve this
rows = int(input())
matrix = []

for _ in range(rows):
    matrix += [int(num) for num in input().split(", ")]

print(matrix)
