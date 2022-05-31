def ascii_range(char_1, char_2):
    ascii_list = []
    for i in range(ord(char_1) + 1, ord(char_2)):
        ascii_list.append(chr(i))
    result = " ".join(ascii_list)
    return result


char_1 = input()
char_2 = input()

print(ascii_range(char_1, char_2))
