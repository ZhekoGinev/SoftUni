class Vehicle:
    def __init__(self, mileage: int, max_speed=150) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []
