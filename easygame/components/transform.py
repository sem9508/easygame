from pygame import Rect

class Transform2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.rect = Rect(x, y, width, height)