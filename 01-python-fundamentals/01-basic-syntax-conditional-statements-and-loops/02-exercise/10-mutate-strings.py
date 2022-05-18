str_a = input()
str_b = input()

for index, char in enumerate(str_b):
    if str_a[index] == str_b[index]:
        continue
    else:
        str_a = str_a[:index] + str_b[index] + str_a[index + 1:]
        print(str_a)

# old solution using list instead of slicing
# temp = list(str_a)
# for char in range(len(str_a)):
#     if str_a[char] == str_b[char]:
#         continue
#     else:
#         temp[char] = str_b[char]
#         str_a = "".join(temp)
#         print(first_string)
