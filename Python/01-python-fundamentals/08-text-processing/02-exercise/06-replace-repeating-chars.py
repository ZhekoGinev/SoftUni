text = list(input())
result = text[0]
for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        result += text[i]

print(result)