import pygame

class Input(object):
    def __init__(self):
        # Determine whether the user has quit the application
        self.has_quitted = False

    def update(self):
        # Iterate over all user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.has_quitted = True