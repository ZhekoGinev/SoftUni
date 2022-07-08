from collections import defaultdict
from itertools import chain

sides = defaultdict(list)

while True:
    data = input()
    if data == "Lumpawaroo":
        break

    if ' | ' in data:
        delimiter = " | "
    elif " -> " in data:
        delimiter = " -> "
    data = data.split(delimiter)

    all_users = sides.values()
    all_users = list(chain(*all_users))

    if delimiter == " | ":
        side = data[0]
        user = data[-1]
        if user not in all_users:
            sides[side].append(user)

    elif delimiter == " -> ":
        user = data[0]
        side = data[-1]
        # change side
        if user in all_users:
            for side_users in sides.values():
                if user in side_users:
                    side_users.remove(user)
            sides[side].append(user)
            
        elif side not in sides and user not in all_users:
            sides[side].append(user)
        elif user not in all_users:
            sides[side].append(user)
            
        print(f"{user} joins the {side} side!")


for side, users in sides.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")