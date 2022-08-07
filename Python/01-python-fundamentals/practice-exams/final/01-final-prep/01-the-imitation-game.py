msg = input()

while True:
    data = input().split("|")
    if "Decode" in data:
        break

    action = data[0]
    if action == "Move":
        n = int(data[1])
        msg = msg[n:] + msg[:n]
    elif action == "Insert":
        index = int(data[1])
        value = data[2]
        msg = msg[:index] + value + msg[index:]
    elif action == "ChangeAll":
        substr = data[1]
        new_str = data[2]
        msg = msg.replace(substr, new_str)

print(f"The decrypted message is: {msg}")
