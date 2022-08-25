vehicles = input().split(">>")
classes = ("family", "heavyDuty", "sports")
total = 0

for v in vehicles:
    tax = 0
    v = v.split()
    v_type = v[0]
    years = int(v[1])
    mileage = int(v[2])

    if v_type not in classes:
        print("Invalid car type.")
        continue

    if v_type == "family":
        tax = mileage // 3000 * 12 + (50 - years * 5)
        print(f"A {v_type} car will pay {tax:.2f} euros in taxes.")
    
    elif v_type == "heavyDuty":
        tax = mileage // 9000 * 14 + (80 - years * 8)
        print(f"A {v_type} car will pay {tax:.2f} euros in taxes.")
    
    elif v_type == "sports":
        tax = mileage // 2000 * 18 + (100 - years * 9)
        print(f"A {v_type} car will pay {tax:.2f} euros in taxes.")

    total += tax

print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")