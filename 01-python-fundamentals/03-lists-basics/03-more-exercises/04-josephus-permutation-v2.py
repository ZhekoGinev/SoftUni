from collections import deque

people = deque(input().split())
k = int(input())
executed = []

while len(people) > 0:
    people.rotate(-k + 1)
    executed.append(people.popleft())

print(f"[{','.join(executed)}]")
