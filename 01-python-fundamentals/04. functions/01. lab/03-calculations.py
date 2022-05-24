def calculate(first_number, second_number, operation):
    if operation == "add":
        return first_number + second_number
    if operation == "subtract":
        return first_number - second_number
    if operation == "multiply":
        return first_number * second_number
    if operation == "divide":
        return first_number // second_number


operation = input()
x = int(input())
y = int(input())

print(calculate(x, y, operation))
