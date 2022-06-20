voldemort = False
while True:
    name = input()
    if name == "Welcome!":
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        voldemort = True
        break
    else:
        length = len(name)
        if length < 5:
            school = "Gryffindor."
        elif length == 5:
            school = "Slytherin."
        elif length == 6:
            school = "Ravenclaw."
        elif length > 6:
            school = "Hufflepuff."
        print(f"{name} goes to {school}")

if not voldemort:
    print("Welcome to Hogwarts.")
