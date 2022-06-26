days = int(input())
daily_plunder = int(input())
expected = float(input())
plunder = 0

for day in range(1, days + 1):
    plunder += daily_plunder
    if day % 3 == 0:
        plunder += daily_plunder * 0.5
    if day % 5 == 0:
        plunder *= 0.7

if plunder >= expected:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    percent = plunder / expected * 100
    print(f"Collected only {percent:.2f}% of the plunder.")