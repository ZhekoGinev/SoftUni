import os, sys
from collections import defaultdict

os.chdir(sys.path[0])

matches = defaultdict(int)
sanitzed_text = ''

with open('resources/Words Count/words.txt') as words_handle:
    words = words_handle.read().split()

with open('resources/Words Count/text.txt') as text_handle:
    text = text_handle.read()


for ch in text:
    if ch.isalnum() or ch == ' ' or ch == '\n':
        sanitzed_text += ch
    else:
        sanitzed_text += ' '

for word in sanitzed_text.split():
    if word.lower() in words:
        matches[word.lower()] += 1

with open('matches.txt', 'w') as matches_handle:
    for word, count in sorted(matches.items(), key=lambda x: -x[1]):
        print(f"{word} - {count}", file=matches_handle)