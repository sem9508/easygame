import pygame
from .baseobject import BaseObject
from ..managers import AnimationManager

class Animator:
    def __init__(self, ParentObject, animation_manager : AnimationManager, start_animation):
        if not issubclass(type(ParentObject), BaseObject):
            raise AttributeError(f'\n\nNot a Subclass of {BaseObject.__name__}, possible solutions:\n - super().__init__()\n - Inherit {BaseObject.__name__} in your class.\n')
        self.ParentObject = ParentObject
        self.animation_manager = animation_manager
        self.current_frame = 0
        self.selected_animation = None
        self.selected_animation_frames = None

        self.switch_animation(start_animation)

    def switch_animation(self, animation_name):
        self.current_frame = 0
        self.selected_animation = animation_name
        self.selected_animation_frames = self.animation_manager.sequence_database[self.selected_animation]

    def update(self):
        self.current_frame += 1
        if self.current_frame > len(self.selected_animation_frames)-1:
            self.current_frame = 0

    def get_frame(self):
        return self.animation_manager.frame_database[self.selected_animation_frames[self.current_frame]]