herd = input().split(", ")
herd.reverse()
if herd[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    next_sheep = herd.index("wolf")
    print(f"Oi! Sheep number {next_sheep}! " +
          "You are about to be eaten by a wolf!")
