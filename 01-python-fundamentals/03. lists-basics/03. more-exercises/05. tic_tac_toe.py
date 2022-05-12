field = []
for row in range(3):
    field.append(input().split())

horizontal_lines = [row for row in field]
vertical_lines = []
diagonal_lines = [  # hardcoidng /facepalm
    [field[0][0], field[1][1], field[2][2]],
    [field[0][2], field[1][1], field[2][0]]
]

for col in zip(*field):
    vertical_lines.append(list(col))

player1 = ['1', '1', '1']
player2 = ['2', '2', '2']

winners = horizontal_lines + vertical_lines + diagonal_lines

if player1 in winners:
    result = "First player won"
elif player2 in winners:
    result = "Second player won"
else:
    result = "Draw!"

print(result)
# I really don't like this solution even though it works.
# should be re-written once my IQ goes above 42
