key = int(input())
number_of_chars = int(input())

message = ""

for _ in range(number_of_chars):
    message += chr(ord(input()) + key)

print(message)
