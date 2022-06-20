class Rhombus:
    def __init__(self, size: int) -> None:
        self.size = size
    
    def render(self):
        shape = []
        for i in range(1, self.size + 1):
            shape.append(" " * (self.size - i) + "* " * i)
            
        for j in range(self.size - 1, 0, -1):
            shape.append(" " * (self.size - j) + "* " * j)
        print('\n'.join(shape))


size = int(input())

r = Rhombus(size)

r.render()