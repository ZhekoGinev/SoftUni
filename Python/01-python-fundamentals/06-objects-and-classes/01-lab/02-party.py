class Party:
    def __init__(self) -> None:
        self.people = []

    def add(self, name):
        self.people.append(name)


party = Party()

while True:
    name = input()
    if name == "End":
        break
    party.add(name)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")