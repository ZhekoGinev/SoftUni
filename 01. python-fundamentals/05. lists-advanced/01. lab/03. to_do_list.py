to_do_list = []

while True:
    note = input()
    if note == "End":
        break
    else:
        to_do_list.append(note.split("-"))

to_do_list = [task[1]
              for task in sorted(to_do_list, key=lambda task: int(task[0]))]

print(to_do_list)

# to_do_list = [0] * 10

# while True:
#     note = input()
#     if note == "End":
#         break
#     else:
#         token = note.split("-")
#         priority = int(token[0]) - 1
#         task = token[1]
#         to_do_list.pop(priority)
#         to_do_list.insert(priority, task)

# to_do_list = [i for i in to_do_list if i != 0]
# print(to_do_list)


# to_do_list = []

# while True:
#     note = input()
#     if note == "End":
#         break
#     else:
#         to_do_list.append(note)

# to_do_list.sort()
# to_do_list = [task[2:] for task in to_do_list if int(task[0]) >= 1]


# for i in to_do_list:
#     if i[0] == "-":
#         to_do_list.append(i[1:])
#         to_do_list.remove(i)


# print(to_do_list)
