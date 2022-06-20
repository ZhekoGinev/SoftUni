num_of_msgs = int(input())

for _ in range(num_of_msgs):
    code = int(input())
    if code > 88:
        print("Bye.")
    elif code < 86 or code == 87:
        print("GREAT!")
    elif code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
