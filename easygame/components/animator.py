import pygame
from .baseobject import BaseObject

class Animator:
    def __init__(self, ParentObject, animation_manager):
        if not issubclass(type(ParentObject), BaseObject):
            raise AttributeError(f'\n\nNot a Subclass of {BaseObject.__name__}, possible solutions:\n - super().__init__()\n - Inherit {BaseObject.__name__} in your class.\n')
        self.ParentObject = ParentObject
        self.animation_manager = animation_manager