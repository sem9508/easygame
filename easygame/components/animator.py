import pygame
from .baseobject import BaseObject
from ..managers import AnimationManager
from ..utils import Timer

class Animator:
    def __init__(self, ParentObject, animation_manager: AnimationManager, start_animation, frame_duration: float):
        if not issubclass(type(ParentObject), BaseObject):
            raise AttributeError(f'\n\nNot a Subclass of {BaseObject.__name__}, possible solutions:\n - super().__init__()\n - Inherit {BaseObject.__name__} in your class.\n')
        self.ParentObject = ParentObject
        self.animation_manager = animation_manager
        self.frame_index = 0
        self.selected_animation_name = None
        self.selected_animation_frame_names = None

        # Create a Timer instance to control frame duration
        self.frame_timer = Timer(frame_duration)

        self.switch_animation(start_animation)

    def switch_animation(self, animation_name):
        self.frame_index = 0
        self.frame_timer.reset()
        self.selected_animation_name = animation_name
        self.selected_animation_frame_names = self.animation_manager.sequence_database[self.selected_animation_name]


    def update(self, dt):
        if self.frame_timer.update(dt):
            self.frame_index += 1
            if self.frame_index > len(self.selected_animation_frame_names) - 1:
                self.frame_index = 0
            self.frame_timer.reset()

    def get_frame(self):
        return self.animation_manager.frame_database[self.selected_animation_frame_names[self.frame_index]]
