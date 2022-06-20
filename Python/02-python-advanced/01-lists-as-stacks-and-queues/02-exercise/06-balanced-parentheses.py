from collections import deque

parentheses = deque(list(input()))
max_rotations = len(parentheses) ** 2  # ain't stupid if it works

is_balanced = True


while len(parentheses) > 0:
    match = False
    s = parentheses[0]
    parentheses.rotate(-1)
    if s == '(' and parentheses[0] == ')':
        match = True
    elif s == '[' and parentheses[0] == ']':
        match = True
    elif s == '{' and parentheses[0] == '}':
        match = True

    max_rotations -= 1

    if match:
        parentheses.popleft()
        parentheses.pop()

    if max_rotations < 0:
        is_balanced = False
        break


if is_balanced:
    print("YES")
else:
    print("NO")
