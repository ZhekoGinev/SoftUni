deck = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    left_half = deck[:len(deck)//2]  # upper half of the deck
    right_half = deck[len(deck)//2:]  # lower half of the deck
    deck = []  # we have empty deck right now split in 2 halves
    for card in range(len(left_half)):  # shuffle them back together
        deck.append(left_half[card])
        deck.append(right_half[card])

print(deck)
