key = input()

while True:
    data = input().split(">>>")
    if "Generate" in data:
        break

    action = data[0]

    if action == "Contains":
        substring = data[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case = data[1]
        start = int(data[2])
        end = int(data[3])
        if case == "Upper":
            key = key[:start] + key[start:end].upper() + key[end:]
        elif case == "Lower":
            key = key[:start] + key[start:end].lower() + key[end:]
        print(key)

    elif action == "Slice":
        start = int(data[1])
        end = int(data[2])
        key = key[:start] + key[end:]
        print(key)

print(f"Your activation key is: {key}")
