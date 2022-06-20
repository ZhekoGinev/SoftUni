n = int(input())

for _ in range(n):
    data = input()
    if any(symbol in data for symbol in (',', '.', '_')):  # see bottom
        print(f"{data} is not pure!")
    else:
        print(f"{data} is pure.")

# alternative condition: "," in data or "." in data or "_" in data
# you can have a much larger set of symbols using any()
