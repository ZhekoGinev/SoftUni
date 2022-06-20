while True:
    data = input()
    if data == "End":
        break
    elif data == "SoftUni":
        continue
    else:
        for ch in data:
            print(ch * 2, end="")
        print()
