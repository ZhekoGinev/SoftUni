text = input()
for i, ch in enumerate(text):
    if ch == ":":
        print(text[i:i+2])