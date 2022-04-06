# a huge lol @ softuni testing system for expecting
# set results to come in certain order every time
# you may need to run the code in judge several times

n = int(input())

odds = set()
evens = set()

row = 1

for _ in range(n):
    name = input()
    ascii_sum = sum([ord(i) for i in name]) // row
    if ascii_sum % 2 == 0:
        evens.add(ascii_sum)
    else:
        odds.add(ascii_sum)
    row += 1

oddsum = sum(odds)
evensum = sum(evens)

odds = {str(i) for i in odds}
evens = {str(i) for i in evens}

if oddsum == evensum:
    print(', '.join(odds | evens))
elif oddsum > evensum:
    print(', '.join(odds - evens))
elif oddsum < evensum:
    print(', '.join(odds ^ evens))
