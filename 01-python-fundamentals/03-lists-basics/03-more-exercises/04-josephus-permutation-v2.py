from collections import deque

people = deque(input().split())
k = int(input())
executed = []

while people:
    people.rotate(-k + 1)
    executed.append(people.popleft())

print(f"[{','.join(executed)}]")
