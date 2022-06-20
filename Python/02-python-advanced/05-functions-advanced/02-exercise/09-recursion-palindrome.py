# I spent more than an hour on this "simple" algorithm
def palindrome(word, index):
    if index >= len(word):
        return f"{word} is a palindrome"
    if word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)
