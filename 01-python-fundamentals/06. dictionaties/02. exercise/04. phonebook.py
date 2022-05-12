from collections import defaultdict
phonebook = defaultdict(str)
search = []

while True:
    command = input()
    if not "-" in command:
        search_contacts_number = int(command)
        break
    else:
        command = command.split("-", maxsplit=1)
        contact = command[0]
        number = command[1]
        phonebook[contact] = number

for _ in range(search_contacts_number):
    name = input()
    search.append(name)

for name in search:
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
