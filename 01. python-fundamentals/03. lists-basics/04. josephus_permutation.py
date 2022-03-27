list_of_people = input().split()
execute_every_nth = int(input())

execute_order = []
counter = 0
index = 0

while len(list_of_people) > 0:
    counter += 1
    if counter == execute_every_nth:
        execute_order.append(list_of_people.pop(index))
        counter = 0
    else:
        index += 1
    if index >= len(list_of_people):
        index = 0

formatted_output = f"[{','.join(execute_order)}]"
print(formatted_output)
