rows = int(input())
matrix = []

for _ in range(rows):
    data = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
    matrix.append(data)

print(matrix)
