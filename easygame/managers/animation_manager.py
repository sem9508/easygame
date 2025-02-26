import pygame

class AnimationManager:
    def __init__(self):
        self.database = {}
        self.animation_frames = {}

    def add_animation_sequence(self, name_in_database, path_to_folder, frame_durations, file_type):
        base_name = path_to_folder.split('/')[-1]
        animation_data = []

        i = 0
        for frame in frame_durations:
            animation_id = base_name + '_' + str(i)
            animation_path = path_to_folder + '/' + animation_id + file_type
            animation_image = pygame.image.load(animation_path).convert_alpha()
            self.animation_frames[animation_id] = animation_image.copy()

            for j in range(frame):
                animation_data.append(animation_id)

            i += 1

        self.database[name_in_database] = animation_data
