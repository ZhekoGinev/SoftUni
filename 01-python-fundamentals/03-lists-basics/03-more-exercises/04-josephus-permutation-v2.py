from collections import deque

people = deque(input().split())
k = int(input())
executed = []

while people:
    people.rotate(-k)
    executed.append(people.pop())

print(f"[{','.join(executed)}]")
