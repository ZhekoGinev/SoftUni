text = input().lower()
words = ('sand', 'water', 'fish', 'sun')
counter = 0
for word in words:
    counter += text.count(word)

print(counter)
