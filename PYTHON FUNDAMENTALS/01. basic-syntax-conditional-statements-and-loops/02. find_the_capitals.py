text = input()
capital_indices = []

for index, char in enumerate(text):
    if char.isupper():
        capital_indices.append(index)

print(capital_indices)
