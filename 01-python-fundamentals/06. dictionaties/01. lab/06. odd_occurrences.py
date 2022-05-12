from collections import defaultdict
elements = input().lower().split()
elements_dict = defaultdict(int)

for e in elements:
    elements_dict[e] += 1

for element, value in elements_dict.items():
    if value % 2 != 0:
        print(element, end=" ")
