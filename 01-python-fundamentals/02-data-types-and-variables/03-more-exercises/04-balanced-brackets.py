number_of_lines = int(input())
brackets = ""
is_balanced = False

# we only care about the brackets
for _ in range(number_of_lines):
    data = input()
    if data == "(" or data == ")":
        brackets += data

# nested brackets are considered unbalanced
# so it becomes a very easy check
for i in range(0, len(brackets), 2):
    if brackets[i] == "(" and brackets[i + 1] == ")":
        is_balanced = True
    else:
        is_balanced = False
        break

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
