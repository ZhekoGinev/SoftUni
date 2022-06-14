people = [1] * int(input())
lifts = [int(i) for i in input().split()]
max_capacity = len(lifts) * 4

for lift, _ in enumerate(lifts):
    while lifts[lift] < 4 and people:
        lifts[lift] += people.pop()
    if not people:
        break

current_capacity = sum(lifts)

lifts = ' '.join(str(s) for s in lifts)

if people:
    print(f"There isn't enough space! {len(people)} people in a queue!")
    print(lifts)
elif max_capacity > current_capacity:
    print("The lift has empty spots!")
    print(lifts)
elif max_capacity == current_capacity:
    print(lifts)