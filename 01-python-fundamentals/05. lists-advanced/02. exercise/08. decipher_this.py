message = input().split()

decipher = []


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
        last_ch = ''.join(word.pop(0))
        second_ch = ''.join(word.pop())
        rest = ''.join(word)

        decipher.append(first_ch + second_ch + rest + last_ch)
    else:  # if it's a small word get only 1 or 2 letters
        decipher.append(first_ch + ''.join(word))

print(' '.join(decipher))
