rows = int(input())
matrix = []
diagonal_sum = 0

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

for i in range(rows):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
