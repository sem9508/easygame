class Timer:
    def __init__(self, target_time):
        self.timer = 0
        self.target_time = target_time

    def update(self, dt):
        """
        Possible return values:

        - True: Timer has reached target_time
        - False: Timer has not reached target_time
        """
        if self.timer > self.target_time:
            return True
        
        else:
            self.timer += dt
            return False

    def reset(self):
        self.timer = 0