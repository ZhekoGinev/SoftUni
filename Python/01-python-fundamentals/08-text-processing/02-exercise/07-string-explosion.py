text = list(input())
strength = 0

for i, ch in enumerate(text):
    if ch == ">":
        strength += int(text[i + 1])
    if strength > 0 and ch.isalnum():
        text[i] = "#"
        strength -= 1
        
print("".join(text).replace("#", ""))
