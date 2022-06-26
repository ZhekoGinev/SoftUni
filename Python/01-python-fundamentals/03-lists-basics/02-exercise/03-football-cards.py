cards = input().split()

team_a = ["A-" + str(i) for i in range(1, 12)]
team_b = ["B-" + str(i) for i in range(1, 12)]

is_terminated = False

for player in cards:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break


if not is_terminated:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
