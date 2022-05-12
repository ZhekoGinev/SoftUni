factor = int(input())
count = int(input())

list_of_matches = []

for num in range(1, count + 1):
    list_of_matches.append(num * factor)

print(list_of_matches)
