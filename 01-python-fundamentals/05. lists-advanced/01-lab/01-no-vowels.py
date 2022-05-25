text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']


no_vowels = [char for char in text if char not in vowels]
no_vowels = "".join(no_vowels)

print(no_vowels)
