n = int(input())

unique_names = set()

for _ in range(n):
    unique_names.add(input())

print('\n'.join(unique_names))
