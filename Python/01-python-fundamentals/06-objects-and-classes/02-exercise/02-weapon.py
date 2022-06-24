class Weapon:
    def __init__(self, bullets: int) -> None:
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f'shooting...'
        else:
            return f"no bullets left"

    def __repr__(self) -> str:
        return f"Remaining bullets: {self.bullets}"
