from .transform import Transform2D

class BaseObject:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.transform = Transform2D(x, y, width, height)
