cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    deck_a = cards[:len(cards)//2]  # upper half of the deck
    deck_b = cards[len(cards)//2:]  # lower half of the deck
    cards = []  # we have empty deck right now split in 2 halves
    for card in range(len(deck_a)):  # shuffle them back together
        cards.append(deck_a[card])
        cards.append(deck_b[card])

print(cards)
