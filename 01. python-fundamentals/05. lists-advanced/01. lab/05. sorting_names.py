names = input().split(", ")

# ref https://scripteverything.com/sort-list-by-string-length-python/
sorted_list = sorted(names, key=lambda x: (-len(x), x))

print(sorted_list)
