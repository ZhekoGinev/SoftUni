first_sentence = input().split(", ")
second_sentence = input().split(", ")

matches = []

for word in first_sentence:
    for w in second_sentence:
        if word in w and word not in matches:
            matches.append(word)

print(matches)
