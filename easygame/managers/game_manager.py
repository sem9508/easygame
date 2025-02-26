
from ..components.camera import Camera2D
from ..utils.math_functions import calculate_dt
import pygame

class GameManager():
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.camera = Camera2D(self)
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.run = True
        self.previous_frame_time = 0

    def get_dt(self):
        dt, self.previous_frame_time = calculate_dt(pygame.time.get_ticks(), self.previous_frame_time)
        return dt
