from .transform import Transform2D

class BaseObject:
    def __init__(self):
        self.transform = Transform2D()
