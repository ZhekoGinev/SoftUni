chat = []

while True:
    command = input()
    if command == "end":
        break
    tokens = command.split()
    command = tokens[0]
    message = tokens[1]

    if command == "Chat":
        chat.append(message)
    
    elif command == "Delete" and message in chat:
        chat.remove(message)

    elif command == "Edit" and message in chat:
        new = tokens[-1]
        chat[chat.index(message)] = new
    
    elif command == "Pin" and message in chat:
        msg = message
        chat.remove(message)
        chat.append(msg)

    elif command == "Spam":
        messages = tokens[1:]
        for i in messages:
            chat.append(i)

chat = '\n'.join(str(i) for i in chat)
print(f"{chat}")