n = int(input())

periodic_table = set()

for _ in range(n):
    element = input().split()
    for compound in element:
        periodic_table.add(compound)

print('\n'.join(periodic_table))
