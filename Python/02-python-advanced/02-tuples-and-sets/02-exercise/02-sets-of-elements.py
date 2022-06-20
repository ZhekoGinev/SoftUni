size_set_1, size_set_2 = input().split()
set_1 = set()
set_2 = set()

for _ in range(int(size_set_1)):
    set_1.add(input())

for _ in range(int(size_set_2)):
    set_2.add(input())

print('\n'.join(set_1 & set_2))
