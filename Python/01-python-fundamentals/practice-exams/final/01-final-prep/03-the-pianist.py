pieces = {}

n = int(input())

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]

while True:
    data = input()
    if data == "Stop":
        break

    data = data.split("|")
    action = data[0]
    piece = data[1]

    if action == "Add":
        composer = data[2]
        key = data[3]
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    
    elif action == "ChangeKey":
        if piece in pieces:
            new_key = data[-1]
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")