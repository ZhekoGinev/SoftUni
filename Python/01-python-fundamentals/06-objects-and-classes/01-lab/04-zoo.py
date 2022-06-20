class Zoo:
    __animals = 0

    def __init__(self, name) -> None:
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\n\
Total animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\n\
Total animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\n\
Total animals: {self.__animals}"


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_animals = int(input())

for _ in range(number_of_animals):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

type_of_animal = input()
print(zoo.get_info(type_of_animal))
