rows = int(input())
matrix = []

prime_diag = []
secondary_diag = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

for i in range(rows):
    prime_diag.append(matrix[i][i])

for j in range(rows):
    secondary_diag.append(matrix[j][len(matrix) - 1 - j])

pd_seq = ', '.join([str(i) for i in prime_diag])
sd_seq = ', '.join([str(i) for i in secondary_diag])

print(f"Primary diagonal: {pd_seq}. Sum: {sum(prime_diag)}")
print(f"Secondary diagonal: {sd_seq}. Sum: {sum(secondary_diag)}")
