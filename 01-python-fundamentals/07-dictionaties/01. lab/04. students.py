data = {}
course = ""
while True:
    command = input()
    if ":" in command:
        tokens = command.split(":")
        name = tokens[0]
        id = int(tokens[1])
        course = tokens[2]
        if course in data:
            data[course] += [[name, id]]
        else:
            data[course] = [[name, id]]
    else:
        course = command.replace("_", " ")
        break

for i in data[course]:
    name = i[0]
    id = i[1]
    print(f"{name} - {id}")
