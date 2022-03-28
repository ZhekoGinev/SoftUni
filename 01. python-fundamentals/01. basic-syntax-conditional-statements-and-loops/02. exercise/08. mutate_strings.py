first_string = input()
second_string = input()
temp = list(first_string)
for char in range(len(first_string)):
    if first_string[char] == second_string[char]:
        continue
    else:
        temp[char] = second_string[char]
        first_string = "".join(temp)
        print(first_string)
