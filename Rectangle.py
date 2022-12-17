class Rectangle:
    x1 = 0
    y1 = 0
    x2 = 0 
    y2 = 0
    bground = "white"
    bound = "black"
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, bground = "white", bound = "black") -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.bground = bground
        self.bound = bound
    def drawObj(self, cas):
        self.obj = cas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline = self.bound, fill = self.bground)
    def deleteObj(self, cas):
        if self.hinh:
            cas.delete(self.hinh)
    def isBound(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return 1
        else:
            return 0