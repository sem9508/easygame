from .baseobject import BaseObject

class PhysicsObject2D:
    def __init__(self, ParentObject):
        if not issubclass(type(ParentObject), BaseObject):
            raise AttributeError(f'\n\nNot a Subclass of {BaseObject.__name__}, possible solutions:\n - super().__init__()\n - Inherit {BaseObject.__name__} in your class.\n')
        self.ParentObject = ParentObject
        self.velocity = [0, 0]
        self.max_velocity = [0, 0]
        self.override_max_velocity = True
        self.acceleration = [0, 0]
        self.mass = 1.0
        self.horizontal_friction_force = 0
        self.vertical_friction_force = 0
        self.use_friction = False

    def apply_force(self, force):
        self.acceleration[0] += force[0] / self.mass
        self.acceleration[1] += force[1] / self.mass

    def add_acceleration(self, acceleration):
        self.acceleration[0] += acceleration[0]
        self.acceleration[1] += acceleration[1]

    def add_velocity(self, velocity):
        self.velocity[0] += velocity[0]
        self.velocity[1] += velocity[1]

    def set_velocity(self, velocity):
        self.velocity = velocity

    def calc_friction(self):
        if self.velocity[0] == 0:
            friction_force_x = 0
        else:
            friction_force_x = -self.velocity[0]/abs(self.velocity[0]) * self.horizontal_friction_force

        if self.velocity[1] == 0:
            friction_force_y = 0
        else:
            friction_force_y = -self.velocity[1]/abs(self.velocity[1]) * self.vertical_friction_force

        return [friction_force_x, friction_force_y]

    def update(self, dt):
        if self.use_friction:
            self.apply_force(self.calc_friction())

        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

        if self.override_max_velocity == False:
            if abs(self.velocity[0]) > self.max_velocity[0]:
                if self.velocity[0] < 0:
                    self.velocity[0] = -self.max_velocity[0]
                else:
                    self.velocity[0] = self.max_velocity[0]
            if abs(self.velocity[1]) > self.max_velocity[1]:
                if self.velocity[1] < 0:
                    self.velocity[1] = -self.max_velocity[1]
                else:
                    self.velocity[1] = self.max_velocity[1]

        self.ParentObject.transform.x += self.velocity[0] * dt
        self.ParentObject.transform.y += self.velocity[1] * dt

        self.acceleration = [0, 0]