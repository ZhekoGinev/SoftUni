text = input()

for char in sorted(set(text)):
    print(f"{char}: {text.count(char)} time/s")
