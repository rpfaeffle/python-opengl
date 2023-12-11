import pygame
import sys

from core.input import Input

class Base(object):
    def __init__(self, screen_size = [520, 520]):
        # Initialize pygame
        pygame.init()
        # Indicate rendering details
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # Use core for platform compatability
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        # create and display the window
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        # Set text that appears on the top bar of the window
        pygame.display.set_caption("Graphics Window")

        # Set important variables
        self.is_running = True
        self.clock = pygame.time.Clock()

        # Manage user input
        self.input = Input()

    # implement by initializing the class
    def initialize(self):
        pass

    # implement by initializing the class
    def update(self):
        pass

    def run(self):
        ## Startup
        self.initialize()

        while self.is_running:
            self.update()
            # Display image on screen
            pygame.display.flip()

            self.input.update()
            if self.input.has_quitted:
                self.is_running = False

            # Limit refresh rate to 60 FPS
            self.clock.tick(60)

        # Shudown application
        pygame.quit()
        sys.exit()