distances = [int(i) for i in input().split()]
total = 0

while len(distances) > 0:
    index = int(input())
    if index < 0:
        value = distances[0]
        distances[0] = distances[-1]
    elif index > len(distances) - 1:
        value = distances[-1]
        distances[-1] = distances[0]
    elif 0 <= index < len(distances):
        value = distances.pop(index)

    total += value
    for i, distance in enumerate(distances):
        if distance <= value:
            distances[i] += value
        else:
            distances[i] -= value

print(total)
