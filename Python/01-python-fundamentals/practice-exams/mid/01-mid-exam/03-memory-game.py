elements = input().split()
moves = 0

while True:

    data = input()

    if data == "end" and elements:
        print(f"Sorry you lose :(")
        print(" ".join(elements))
        break

    if not elements:
        print(f"You have won in {moves} turns!")
        break

    moves += 1
    first, second = [int(i) for i in data.split()]

    bigger = max(first, second) # since I'm using pop() I need to
    smaller = min(first, second) # remove the bigger index first

    if ( # same index or out of bound
        first == second
        or not 0 <= first < len(elements)
        or not 0 <= second < len(elements)
    ):
        elements.insert(len(elements) // 2, f"-{moves}a")
        elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[first] == elements[second]:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        elements.pop(bigger)
        elements.pop(smaller)

    elif elements[first] != elements[second]:
        print("Try again!")