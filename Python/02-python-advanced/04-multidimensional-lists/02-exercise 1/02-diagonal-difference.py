rows = int(input())
matrix = []

prime_diag = []
secondary_diag = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

for i in range(rows):
    prime_diag.append(matrix[i][i])

for j in range(rows):
    secondary_diag.append(matrix[j][len(matrix) - 1 - j])


print(abs(sum(prime_diag) - sum(secondary_diag)))
