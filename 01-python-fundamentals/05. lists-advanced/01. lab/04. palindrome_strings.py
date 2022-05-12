words = input().split()
palindrome = input()


list_of_palindromes = [word for word in words if word == word[::-1]]

count = list_of_palindromes.count(palindrome)
print(list_of_palindromes)
print(f"Found palindrome {count} times")
