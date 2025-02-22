from .baseobject import BaseObject

class Camera2D(BaseObject):
    def __init__(self):
        super().__init__()
        self.zoom = 1.0

    def apply(self, pos):
        # Transform a world position into a camera-relative position
        return [(pos[0] - self.x) * self.zoom, (pos[1] - self.y) * self.zoom]