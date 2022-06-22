to_do_list = []

while True:
    note = input()
    if note == "End":
        break
    to_do_list.append(note.split("-"))
# sort tasks by their number and add the task to the list
to_do_list = [task[1] for task in sorted(to_do_list, key=lambda task: int(task[0]))]

print(to_do_list)