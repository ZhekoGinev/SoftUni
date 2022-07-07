banned = input().split(", ")
text = input()

for word in banned:
    l = len(word)
    while word in text:
        text = text.replace(word, "*" * l)

print(text)