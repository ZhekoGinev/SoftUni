rows, cols = list(map(int, (input().split(", "))))
matrix = []
matrix_sum = 0

for _ in range(rows):
    data = [int(i) for i in input().split(", ")]
    matrix.append(data)
    matrix_sum += sum(data)

print(matrix_sum)
print(matrix)
