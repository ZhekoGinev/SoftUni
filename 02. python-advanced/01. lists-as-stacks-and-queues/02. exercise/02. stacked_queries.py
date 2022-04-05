# I was feeling cheeky so I implemented the solution with class

class Stack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, number):
        self.__stack.append(number)

    def pop(self):
        self.__stack.pop()

    def max(self):
        return max(self.__stack)

    def min(self):
        return min(self.__stack)

    def length(self):
        return len(self.__stack)

    def __repr__(self) -> str:
        temp = [str(i) for i in self.__stack]
        return f"{', '.join(reversed(temp))}"


n = int(input())

stack = Stack()

for _ in range(n):
    command = input().split()
    action = command[0]
    if action == '1':
        stack.push(int(command[1]))
    elif action == '2' and stack.length() > 0:
        stack.pop()
    elif action == '3' and stack.length() > 0:
        print(stack.max())
    elif action == '4' and stack.length() > 0:
        print(stack.min())

print(stack)
