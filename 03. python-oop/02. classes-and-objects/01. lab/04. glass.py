class Glass:
    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml: int):
        if self.content + ml <= self.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"
