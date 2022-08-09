stops = input()

while True:
    data = input()
    if data == "Travel":
        break

    data = data.split(":")
    action = data[0]
    size = len(stops)

    if action == "Add Stop":
        index = int(data[1])
        if index in range(size):
            stops = stops[:index] + data[2] + stops[index:]

    elif action == "Remove Stop":
        start = int(data[1])
        end = int(data[2])

        if start in range(size) and end in range(size): # and end >= start
            stops = stops[:start] + stops[end+1:]

    elif action == "Switch":
        old_str = data[1]
        new_str = data[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)
    
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")