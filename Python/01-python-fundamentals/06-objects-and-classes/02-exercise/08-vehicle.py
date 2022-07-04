class Vehicle:
    def __init__(self, type, model, price) -> None:
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        result = ""
        if money >= self.price and self.owner == None:
            result = f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
            self.owner = owner
        else:
            if money < self.price:
                result = "Sorry, not enough money"
            elif self.owner is not None:
                result = "Car already sold"

        return result

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self) -> str:
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
