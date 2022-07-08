from collections import defaultdict

resources = defaultdict(int)

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    resources[resource] += quantity

for r, q in resources.items():
    print(f"{r} -> {q}")
