n_of_rows = int(input())
can_escape = True
moves = 1
# init matrix
matrix = []
for _ in range(n_of_rows):
    matrix.append(list(input()))

# find Kate's initial position
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == "k":
            pos = [i, j]
            break

while True:

    row = pos[0]
    col = pos[1]

    if not can_escape:
        print("Kate cannot get out")
        break

    # check adjacent squares and move if empty
    if matrix[row - 1][col] == " ":   # up and [row - 1, col]:
        pos = [row - 1, col]
        matrix[pos[0]][pos[1]] = "#"
        moves += 1
    elif matrix[row + 1][col] == " " and [row + 1, col]:  # down
        pos = [row + 1, col]
        matrix[pos[0]][pos[1]] = "#"
        moves += 1
    elif matrix[row][col - 1] == " " and [row, col - 1]:  # left
        pos = [row, col - 1]
        matrix[pos[0]][pos[1]] = "#"
        moves += 1
    elif matrix[row][col + 1] == " " and [row, col + 1]:  # right
        pos = [row, col + 1]
        matrix[pos[0]][pos[1]] = "#"
        moves += 1

    else:
        can_escape = False

    if (  # if we reach an exit break the loop
        pos[0] == 0
        or pos[0] == len(matrix) - 1
        or pos[1] == 0
        or pos[1] == len(matrix[row]) - 1
    ):
        print(f"Kate got out in {moves} moves")
        break
