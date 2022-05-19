number_of_lines = int(input())

data = ""

is_balanced = False

# I only care about the brackets
for _ in range(number_of_lines):
    ui = input()
    if ui == "(" or ui == ")":
        data += ui

# nested brackets are considered unbalanced
# so it becomes a very easy check
for i in range(0, len(data), 2):
    if data[i] == "(" and data[i + 1] == ")":
        is_balanced = True
    else:
        is_balanced = False
        break

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
