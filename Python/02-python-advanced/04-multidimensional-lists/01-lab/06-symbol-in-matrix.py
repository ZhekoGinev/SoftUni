def find_in_matrix(matrix, element):
    for index, row in enumerate(matrix):
        for i, col in enumerate(row):
            if col == element:
                return index, i


rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

search_for = input()

search_found = find_in_matrix(matrix, search_for)

if search_found:
    print(search_found)
else:
    print(f"{search_for} does not occur in the matrix")
