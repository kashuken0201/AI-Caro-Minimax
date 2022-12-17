from Rectangle import *
class XO(Rectangle):
    # 1 la X, -1 la O
    value = 0
    def __init__(self) -> None:
        super().__init__(0, 0, 0, 0)
        self.value = 0
    def __init__(self, x1=0, y1=0, x2=0, y2=0) -> None:
        super().__init__(x1, y1, x2, y2)
        self.value = 0
    def draw(self, cas):
        super().drawObj(cas)
        dx = (self.x2 - self.x1) / 4
        dy = (self.y2 - self.y1) / 4
        if self.value == 1:
            cas.create_line(self.x1 + dx, self. y1 + dy, self.x2 - dx, self.y2 - dy, fill = "red",width=3)
            cas.create_line(self.x2 - dx, self. y1 + dy, self.x1 + dx, self.y2 - dy, fill = "red",width=3)
        if self.value == -1:
            cas.create_oval(self.x1 + dx, self.y1 + dy, self.x2 - dx, self.y2 - dy, outline = "blue",width=3)
