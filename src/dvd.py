from core.application import Application
from OpenGL.GL import *
import random
import math


def get_random_direction():
    return random.randint(0, 5) + 1


class DVD(Application):
    def __init__(self, screen_size=[520, 520], start_position=[0, 0]):
        super().__init__(screen_size)
        self.x_direction = 1
        self.y_direction = 1
        self.x = start_position[0]
        self.y = start_position[1]

    def initialize(self):
        super().initialize()
        print("Initializing program...")
        self.item_size = 30

    def render(self, context):
        width = self.screen_size[0]
        height = self.screen_size[1]

        # Check if the ball is at the edge of the screen and change direction
        if self.x > width - (self.item_size / 2 + self.x_direction):
            self.x_direction = -1 * get_random_direction()
        elif self.x < -1 * (width - (self.item_size / 2 + self.x_direction)):
            self.x_direction = get_random_direction()

        if self.y > height - (self.item_size / 2 + self.y_direction):
            self.y_direction = -1 * get_random_direction()
        elif self.y < -1 * (height - (self.item_size / 2 + self.y_direction)):
            self.y_direction = get_random_direction()

        # Move the ball
        self.x += self.x_direction
        self.y += self.y_direction

        # Calculate the position of the ball
        vertices = [
            ((self.x - self.item_size / 2) / width, (self.y - self.item_size / 2) / height),
            ((self.x - self.item_size / 2) / width, (self.y + self.item_size / 2) / height),
            ((self.x + self.item_size / 2) / width, (self.y + self.item_size / 2) / height),
            ((self.x + self.item_size / 2) / width, (self.y - self.item_size / 2) / height)
        ]

        glBegin(GL_QUADS)
        time = context['time']
        glColor3f(abs(math.sin(time)), abs(math.cos(time)), abs(math.sin(time + 0.5)))
        for vertex in vertices:
            glVertex2f(*vertex)
        glEnd()

DVD().run()
