from .physicsobject import PhysicsObject2D

class RigidBody2D:
    def __init__(self, ParentObject):
        if not hasattr(ParentObject, PhysicsObject2D.__name__.lower()):
            raise AttributeError(f'\n\nNo component on parent class with variable name {PhysicsObject2D.__name__.lower()} found.\nPlease add that variable with the RigidBody2D component.\n')
        
        self.ParentObject = ParentObject
        self.gravity = 800

    def update(self, dt):
        self.ParentObject.physicsobject2d.add_acceleration([0, self.gravity])