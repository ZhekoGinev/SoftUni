gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    else:
        tokens = command.split()
        status = tokens[0]
        gift = tokens[1]

        if status == 'OutOfStock' and gift in gifts:
            for i, g in enumerate(gifts):
                if g == gift:
                    gifts[i] = None

        elif status == 'Required' and 0 <= int(tokens[-1]) <= len(gifts) - 1:
            gifts[int(tokens[-1])] = gift
            
        elif status == 'JustInCase':
            gifts[-1] = gift

print(' '.join(g for g in gifts if g is not None))