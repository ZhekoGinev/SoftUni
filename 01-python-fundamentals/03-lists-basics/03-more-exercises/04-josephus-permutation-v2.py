# same problem but solved using a queue

from collections import deque

people = deque(input().split())
k = int(input())
executed = []

while len(people) > 0:
    # rotate the circle so person k + 1 goes to index 0
    people.rotate(-k + 1)
    executed.append(people.popleft()) # then we "execute" the person

formatted_output = f"[{','.join(executed)}]"
print(formatted_output)
