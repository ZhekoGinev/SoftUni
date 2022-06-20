divisor = int(input())
boundary = int(input())
largest_divisor = 0
for number in range(boundary, -1, -1):
    if number % divisor == 0:
        largest_divisor = number
        break
print(largest_divisor)
