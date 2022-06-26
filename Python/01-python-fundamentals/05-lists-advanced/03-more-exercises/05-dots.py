n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

# find all positions with "."
points = []
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == ".":
            points.append([i, j])

if len(points) == 0:
    print(0)

elif len(points) == 1:
    print(1)
    
elif len(points) > 1:
    clusters = []
    #create an empty "cluster" for each point
    for i in range(len(points)):
        clusters.append([])

    # get each point and the points it is connected to and append it
    # each cluster represents each point and it's connections
    for i in range(len(points)):
        curr = points[i]
        for p in points:
            if curr == p:  # same element
                continue
            if curr[0] == p[0] and (curr[1] == p[1] - 1 or curr[1] == p[1] + 1):
                clusters[i].append(tuple(p))
            elif curr[1] == p[1] and (curr[0] == p[0] - 1 or curr[0] == p[0] + 1):
                clusters[i].append(tuple(p))
        if len(clusters[i]) > 0:
            clusters[i].append(tuple(curr))


    # remove empty clusters (points that have no connections)
    clusters = sorted([elements for elements in clusters if len(elements) > 0])

    result = []
    # merge elements if they share a common element
    while len(clusters) > 0:
        first_element, *remaining_elements = clusters
        first_element = set(first_element)

        temp_stack = [] # keep the elements that do not match here

        for r in remaining_elements:
            if first_element & set(r):   # if they share an element
                first_element |= set(r)  # merge the two clusters
            else:
                temp_stack.append(r)

        remaining_elements = temp_stack

        result.append(len(first_element))
        clusters = remaining_elements

    print(max(result))