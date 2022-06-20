n = int(input())

guestlist = set()

for _ in range(n):
    guestlist.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        guestlist.remove(guest)

print(len(guestlist))
print('\n'.join(sorted(guestlist)))
