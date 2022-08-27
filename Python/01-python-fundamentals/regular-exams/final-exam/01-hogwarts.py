spell = input()

while True:
    data = input().split()
    if "Abracadabra" in data:
        break

    command = data[0]

    if command == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif command == "Illusion":
        idx = int(data[1])
        letter = data[2]
        if idx in range(len(spell)):
            spell = spell[:idx] + letter + spell[idx + 1 :]
            print("Done!")
        else:
            print("The spell was too weak.")
    
    elif command == "Divination":
        old_str = data[1]
        new_str = data[2]
        if old_str in spell:
            spell = spell.replace(old_str, new_str)
            print(spell)

    elif command == "Alteration":
        substring = data[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")