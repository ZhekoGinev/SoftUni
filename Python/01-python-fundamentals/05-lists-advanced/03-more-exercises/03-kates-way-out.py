n_of_rows = int(input())
can_escape = True

# init matrix
matrix = []
for _ in range(n_of_rows):
    matrix.append(list(input()))

# find Kate's initial position
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == "k":
            position = [i, j]
            break

# track visited squares
visited = [position]

while True:

    row = position[0]
    col = position[1]

    if not can_escape:
        print("Kate cannot get out")
        break

    # check adjacent squares and move if empty
    if matrix[row - 1][col] == " " and [row - 1, col] not in visited:  # up
        position = [row - 1, col]
    elif matrix[row + 1][col] == " " and [row + 1, col] not in visited:  # down
        position = [row + 1, col]
    elif matrix[row][col - 1] == " " and [row, col - 1] not in visited:  # left
        position = [row, col - 1]
    elif matrix[row][col + 1] == " " and [row, col + 1] not in visited:  # right
        position = [row, col + 1]

    else:
        can_escape = False

    if can_escape:  # keep track of visited squares
        visited.append([row, col])

    if (  # if we reach an exit break the loop
        position[0] == 0
        or position[0] == len(matrix) - 1
        or position[1] == 0
        or position[1] == len(matrix[row]) - 1
    ):
        print(f"Kate got out in {len(visited)} moves")
        break
