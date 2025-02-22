class Timer:
    def __init__(self, target_time):
        self.timer = 0
        self.target_time = target_time

    def update(self, dt):
        if self.timer > self.target_time:
            return True
        
        else:
            self.timer += dt
            return False
