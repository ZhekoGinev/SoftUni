class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, hp):
        self.health += hp
