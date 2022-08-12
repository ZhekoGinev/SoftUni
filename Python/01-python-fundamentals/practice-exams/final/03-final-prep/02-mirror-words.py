import re

data = input()

pattern = r"([@#])(([A-z]{3,}))\1{2}([A-z]{3,})\1"

matches = re.findall(pattern, data)
mirror_words = []

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

    mirror_words = [
    f"{match[-2]} <=> {match[-1]}"  # append the pair to mirror_words
    for match in matches
    if match[-2] == match[-1][::-1] # if the first word == reversed second word
    ]

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))
