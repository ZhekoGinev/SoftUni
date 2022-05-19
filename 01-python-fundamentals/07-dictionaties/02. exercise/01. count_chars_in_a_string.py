from collections import defaultdict
text = input()
dict_counter = defaultdict(int)

for c in text:
    if c != " ":
        dict_counter[c] += 1

for k, v in dict_counter.items():
    print(f"{k} -> {v}")
