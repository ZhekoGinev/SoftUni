text = input()

stack = list(text)

while len(stack) > 0:
    print(stack.pop(), end='')
print()
