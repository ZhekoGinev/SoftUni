word = input()
data = input()
while word in data:
    i = data.find(word)
    data = data[:i] + data[i+len(word):]

print(data)