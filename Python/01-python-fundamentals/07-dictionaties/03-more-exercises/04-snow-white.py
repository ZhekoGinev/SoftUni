from collections import defaultdict

dwarves = defaultdict(dict)
names = []

while True:
    
    dwarf = input().split(" <:> ")
    if "Once upon a time" in dwarf:
        break

    name = dwarf[0]
    color = dwarf[1]
    physics = int(dwarf[2])

    if [name, color] not in names:
        dwarves[color][name] = physics
        names.append([name, color])
    elif dwarves[color][name] < physics:
        dwarves[color][name] = physics
   
for color, dwarf in sorted(dwarves.items()):
    print(f"({color}) {dwarf.items()[0][0]} <-> {dwarf.items()[0][1]}")