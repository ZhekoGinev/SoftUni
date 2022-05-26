fires = input().split("#")
total_water = int(input())
total_effort = 0
cells = []

for fire in fires:
    fire_type, cell_value = fire.split(" = ")
    cell_value = int(cell_value)
    cell_effort = cell_value * 0.25
    if (
        (fire_type == 'High' and 81 <= cell_value <= 125 and total_water >= cell_value)
        or (fire_type == 'Medium' and 51 <= cell_value <= 80 and total_water >= cell_value)
        or (fire_type == 'Low' and 1 <= cell_value <= 50 and total_water >= cell_value)
    ):
        total_water -= cell_value
        total_effort += cell_effort
        cells.append(cell_value)

print(f"Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells)}")
