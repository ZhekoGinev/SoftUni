from collections import defaultdict

players = defaultdict(dict)

while True:
    data = input()
    if data == "Season end":
        break

    if " -> " in data:
        data = data.split(" -> ")
        player = data[0]
        position = data[1]
        skill = int(data[2])

        if player not in players.keys():
            players[player][position] = skill
        elif position not in players[player].keys():
            players[player][position] = skill
        elif skill > players[player][position]:
            players[player][position] = skill

    elif " vs " in data: # ifception
        player_1, player_2 = data.split(" vs ")
        if player_1 in players.keys() and player_2 in players.keys(): # if both exist
            player_1_positions = set(players[player_1].keys()) # all positions for a player
            player_2_positions = set(players[player_2].keys())
            if player_1_positions & player_2_positions: # if they share atleast 1 position
                player_1_total = sum(players[player_1].values()) # calculate total skill
                player_2_total = sum(players[player_2].values())
                if player_1_total > player_2_total: # there can be only one *swoosh*
                    players.pop(player_2)
                elif player_2_total > player_1_total:
                    players.pop(player_1)

# sorting skills over 9000
for player, skills in sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(skills.values())} skill")
    for position, skill in sorted(skills.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
