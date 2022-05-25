data = input()
stack = []

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        print(data[stack.pop():i+1])
