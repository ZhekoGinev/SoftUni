n = int(input())
word = input()

full_text = []
filtered_text = []

for _ in range(n):
    text = input()
    full_text.append(text)
    if word in text:
        filtered_text.append(text)

print(full_text)
print(filtered_text)
