# solution feels a bit verbose but it's easy to
# read and understand so I'm sticking with it

def first_max_elem(array_list):
    max_at_index = 0
    for index, element in enumerate(array_list):
        if len(element) > len(array_list[max_at_index]):
            max_at_index = index
    return array_list[max_at_index]


n = int(input())

intersections = []

for _ in range(n):
    first_range = set()
    second_range = set()
    first_intersec, second_intersec = input().split('-')

    start, end = [int(i) for i in first_intersec.split(',')]
    for num in range(start, end + 1):
        first_range.add(num)

    start, end = [int(i) for i in second_intersec.split(',')]
    for num in range(start, end + 1):
        second_range.add(num)

    intersections.append(list(first_range & second_range))

longest = first_max_elem(intersections)

print(f"Longest intersection is {longest} with length {len(longest)}")
