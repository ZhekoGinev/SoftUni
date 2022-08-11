message = input()

while True:
    data = input()
    if data == "Reveal":
        break

    data = data.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        substring = data[1]
        if not substring in message:
            print("error")
        else:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)

    elif action == "ChangeAll":
        old = data[1]
        new = data[2]
        message = message.replace(old, new)
        print(message)

print(f"You have a new text message: {message}")
