message = input().split()
deciphered = []

for word in message:
    word = list(word)
    first_ch = ""
    # get first letter
    for i in word:
        if i.isdigit():
            first_ch += i
    first_ch = chr(int(first_ch))
    # remove digits from word
    word = [i for i in word if i.isalpha()]
    # get second letter, last letter and the remaining word
    if len(word) >= 2:
        last_ch = word.pop(0)
        second_ch = word.pop()
        rest = ''.join(word)
        deciphered.append(first_ch + second_ch + rest + last_ch)
    else:
        deciphered.append(first_ch + ''.join(word))

print(' '.join(deciphered))
