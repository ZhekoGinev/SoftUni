class Party:
    def __init__(self) -> None:
        pass

    people = []

    def add(self, name):
        self.people.append(name)


party = Party()

while True:
    name = input()
    if name == "End":
        break
    else:
        party.add(name)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
