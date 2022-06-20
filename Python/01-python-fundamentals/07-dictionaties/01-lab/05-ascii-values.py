list_of_chars = input().split(", ")
ascii_dict = {char: ord(char) for char in list_of_chars}
print(ascii_dict)
