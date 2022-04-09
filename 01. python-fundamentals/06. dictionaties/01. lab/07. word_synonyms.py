from collections import defaultdict
number_of_words = int(input())
synonym_dict = defaultdict(list)

for _ in range(number_of_words):
    word = input()
    synonym = input()
    synonym_dict[word].append(synonym)

for word, synonym in synonym_dict.items():
    syns = ", ".join(synonym)
    print(f"{word} - {syns}")
