population = [int(i) for i in input().split(", ")]
MIN_WEALTH = int(input())


def richest(i):  # returns the index of the richest person
    return max(list(enumerate(i)), key=lambda x: x[1])[0]


can_distribute = True


for i in range(len(population)):
    r = richest(population)  # wealth of the richest person
    if population[i] < MIN_WEALTH:
        diff = MIN_WEALTH - population[i]
        population[r] -= diff  # take from richest
        population[i] += diff  # give to poorest

# if anyone has less than the minimum distribution is not possible
for i in population:
    if i < MIN_WEALTH:
        can_distribute = False
        break

if can_distribute:
    print(population)
else:
    print("No equal distribution possible")
