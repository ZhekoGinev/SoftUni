data = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    action = command[0]

    if action == "merge":
        start = int(command[1])
        end = int(command[2])
        if start < 0:
            start = 0
        if end >= len(data):
            end = len(data) - 1

        # merge the element at position start with the next one 
        # end minus start number of times
        for _ in range(start, end):
            data[start] += data.pop(start + 1)

    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        parts = []
        # pop the element so we can work with it
        temp = data.pop(index)

        partition_size = len(temp) // partitions

        # append all positions except the last one to parts
        for _ in range(partitions - 1):
            parts.append(temp[:partition_size])
            temp = temp[partition_size:]
        # append the last part to parts
        parts.append(temp)

        # insert the now divided parts back to data
        for i in reversed(parts):
            data.insert(index, i)

print(" ".join([str(i) for i in data]))
