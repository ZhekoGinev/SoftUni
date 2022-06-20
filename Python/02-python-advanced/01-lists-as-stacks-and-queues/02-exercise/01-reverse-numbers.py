numbers = input().split()
stack = []

while len(numbers) > 0:
    stack.append(numbers.pop())

print(" ".join(stack))
