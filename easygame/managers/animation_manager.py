import pygame

class AnimationManager:
    def __init__(self):
        self.sequence_database = {}
        self.frame_database = {}

    def add_animation_sequence(self, name_in_database, path_to_folder, number_of_frames, file_type):
        """
        name_in_database is the identifier when using switch_animation or start_animation in Animator\n\n
        path_to_folder is the relative path to the folder and the folder name should equal the begin of the animation images, for example:

        - player_run
        -- player_run_0.png
        -- player_run_1.png
        \n\n
        frame_durations should be a list with how many frames every frame of the animation is displayed.
        \n\n
        file_type should be the extension of the images. Like: '.png' or '.jpeg'.
        """
        base_name = path_to_folder.split('/')[-1]
        animation_data = []

        for i in range(number_of_frames):
            animation_id = base_name + '_' + str(i)
            animation_path = path_to_folder + '/' + animation_id + file_type
            animation_image = pygame.image.load(animation_path).convert_alpha()
            self.frame_database[animation_id] = animation_image.copy()

            animation_data.append(animation_id)

        self.sequence_database[name_in_database] = animation_data
