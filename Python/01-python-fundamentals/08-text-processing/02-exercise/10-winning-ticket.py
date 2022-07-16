def length(string: str): # only need to check if len >= 6
    left = string[:10]
    right = string[10:]
    min_length = 6
    symbol = 'progamermove'

    #check if symbol repeated 6 or more times exists, else return 1
    for s in ('$', '@', '#', '^'):
        if s * 6 in left and s * 6 in right:
            symbol = s
    if symbol not in ('$', '@', '#', '^'):
        return 1

    # check how many times symbol is repeated in both
    # left and right side and increase accordingly
    for i in range(7, 11):
        if i * symbol in left and i * symbol in right:
            min_length += 1

    return min_length


def is_winner(string: str):
    for i in string:
        if i in ('$', '@', '#', '^'):
            continue
        else:
            return False
    return len(set(string)) == 1


tickets = [
    t.strip()
    if len(t.strip()) == 20
    else "invalid ticket"
    for t in input().split(",")]

for ticket in tickets:

    for s in ticket:
        if s in ('$', '@', '#', '^') and s * 6 in ticket:
            symbol = s
            break

    if ticket == "invalid ticket":
        print(ticket)
    elif is_winner(ticket):
        print(f"ticket \"{ticket}\" - 10{''.join(set(ticket))} Jackpot!")
    elif length(ticket) < 6:
        print(f"ticket \"{ticket}\" - no match")
    else:
        print(f"ticket \"{ticket}\" - {length(ticket)}{symbol}")
