rows, cols = list(map(int, (input().split(", "))))
matrix = []

for _ in range(rows):
    matrix.append([int(i) for i in input().split()])

t_matrix = list(zip(*matrix))

for col in t_matrix:
    print(sum(col))
