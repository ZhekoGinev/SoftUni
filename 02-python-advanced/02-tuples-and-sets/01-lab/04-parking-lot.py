n = int(input())

parking = set()

for _ in range(n):
    command, registration = input().split(', ')
    if command == 'IN':
        parking.add(registration)
    elif command == 'OUT' and registration in parking:
        parking.remove(registration)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')
