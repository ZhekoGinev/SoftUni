password = input()

while True:
    data = input().split()
    if "Done" in data:
        break

    action = data[0]

    if action == "TakeOdd":
        password = password[1::2]
        print(password)

    elif action == "Cut":
        index = int(data[1])
        length = int(data[2])
        substring = password[index:index + length]
        password = password.replace(substring, '', 1)
        print(password)

    elif action == "Substitute":
        old = data[1]
        new = data[2]
        if old in password:
            password = password.replace(old, new)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")