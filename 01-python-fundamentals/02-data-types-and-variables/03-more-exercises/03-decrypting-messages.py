key = int(input())
number_of_chars = int(input())

message = ""

for _ in range(number_of_chars):
    message += chr(ord(input()) + key)

print(message)


# using a function
# key = int(input())
# number_of_chars = int(input())

# message = ""
# decrypted_msg = ""


# def decrypt(character, key):
#     decrypted = chr(ord(character) + key)
#     return decrypted


# for _ in range(number_of_chars):
#     message += input()

# for letter in message:
#     decrypted_msg += decrypt(letter, key)

# print(decrypted_msg)
