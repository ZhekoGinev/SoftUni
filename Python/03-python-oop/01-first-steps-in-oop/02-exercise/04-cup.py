class Cup:
    def __init__(self, size: int, quantity: int) -> None:
        self.size = size
        self.quantity = quantity
    
    def fill(self, quantity: int):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity
    
    def status(self):
        free_space = self.size - self.quantity
        return free_space